from time import time
from modules import DEX, Logger
from utils.tools import gas_checker, repeater
from settings import SLIPPAGE
from config import (
    SPACEFI_CONTRACTS,
    SPACEFI_ROUTER_ABI,
    TOKENS_PER_CHAIN
)


class SpaceFi(DEX, Logger):
    def __init__(self, client):
        super().__init__()
        self.client = client
        self.network = self.client.network.name
        self.router_contract = self.client.get_contract(SPACEFI_CONTRACTS[self.network]['router'], SPACEFI_ROUTER_ABI)

    async def get_min_amount_out(self, from_token_address: str, to_token_address: str, amount_in_wei: int):
        _, min_amount_out = await self.router_contract.functions.getAmountsOut(
            amount_in_wei,
            [
                from_token_address,
                to_token_address
            ]
        ).call()

        return int(min_amount_out - (min_amount_out / 100 * SLIPPAGE))

    @repeater
    @gas_checker
    async def swap(self):
        from_token_name, to_token_name, amount, amount_in_wei = await self.client.get_auto_amount()

        self.logger_msg(*self.client.acc_info, msg=f'Swap on SpaceFi: {amount} {from_token_name} -> {to_token_name}')

        from_token_address = TOKENS_PER_CHAIN[self.network][from_token_name]
        to_token_address = TOKENS_PER_CHAIN[self.network][to_token_name]

        deadline = int(time()) + 1800
        min_amount_out = await self.get_min_amount_out(from_token_address, to_token_address, amount_in_wei)

        await self.client.price_impact_defender(from_token_name, amount, to_token_name, min_amount_out)

        if from_token_name != 'ETH':
            await self.client.check_for_approved(
                from_token_address, SPACEFI_CONTRACTS[self.network]['router'], amount_in_wei
            )

        full_data = (
            min_amount_out,
            [
                from_token_address,
                to_token_address
            ],
            self.client.address,
            deadline
        )

        tx_params = await self.client.prepare_transaction(value=amount_in_wei if from_token_name == 'ETH' else 0)
        if from_token_name == 'ETH':
            transaction = await self.router_contract.functions.swapExactETHForTokens(
                *full_data
            ).build_transaction(tx_params)
        elif to_token_name == 'ETH':
            transaction = await self.router_contract.functions.swapExactTokensForETH(
                amount_in_wei,
                *full_data
            ).build_transaction(tx_params)
        else:
            transaction = await self.router_contract.functions.swapExactTokensForTokens(
                amount_in_wei,
                *full_data
            ).build_transaction(tx_params)

        return await self.client.send_transaction(transaction)
