from config import ERALEND_CONTRACTS, ERALEND_ABI
from utils.tools import gas_checker, repeater
from modules import Landing, Logger


class EraLend(Landing, Logger):
    def __init__(self, client):
        super().__init__()
        self.client = client

        self.landing_contract = self.client.get_contract(ERALEND_CONTRACTS['landing'], ERALEND_ABI)
        self.collateral_contract = self.client.get_contract(ERALEND_CONTRACTS['collateral'], ERALEND_ABI)

    @repeater
    @gas_checker
    async def deposit(self):

        amount, amount_in_wei = await self.client.check_and_get_eth_for_deposit()

        self.logger_msg(*self.client.acc_info, msg=f'Deposit to EraLend: {amount} ETH')

        tx_params = (await self.client.prepare_transaction()) | {
            'to': ERALEND_CONTRACTS['landing'],
            'value': amount_in_wei,
            'data': '0x1249c58b'
        }

        return await self.client.send_transaction(tx_params)

    @repeater
    @gas_checker
    async def withdraw(self):
        self.logger_msg(*self.client.acc_info, msg=f'Withdraw from EraLend')

        liquidity_balance = await self.landing_contract.functions.balanceOfUnderlying(self.client.address).call()

        if liquidity_balance != 0:

            tx_params = await self.client.prepare_transaction()

            transaction = await self.landing_contract.functions.redeemUnderlying(
                liquidity_balance
            ).build_transaction(tx_params)

            return await self.client.send_transaction(transaction)

        else:
            raise RuntimeError(f'Insufficient balance on EraLend!')

    @repeater
    @gas_checker
    async def enable_collateral(self):
        self.logger_msg(*self.client.acc_info, msg=f'Enable collateral on EraLend')

        tx_params = await self.client.prepare_transaction()

        transaction = await self.collateral_contract.functions.enterMarkets(
            [ERALEND_CONTRACTS['landing']]
        ).build_transaction(tx_params)

        return await self.client.send_transaction(transaction)

    @repeater
    @gas_checker
    async def disable_collateral(self):
        self.logger_msg(*self.client.acc_info, msg=f'Disable collateral on EraLend')

        tx_params = await self.client.prepare_transaction()

        transaction = await self.collateral_contract.functions.exitMarket(
            ERALEND_CONTRACTS['landing']
        ).build_transaction(tx_params)

        return await self.client.send_transaction(transaction)
