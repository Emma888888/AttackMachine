import random

from utils.tools import repeater, gas_checker
from modules import Minter, Logger
from config import TOKENS_PER_CHAIN, STARKSTARS_COUNTACTS
from settings import STARKSTARS_NFT_CONTRACTS


class StarkStars(Minter, Logger):
    def __init__(self, client):
        super().__init__()
        self.client = client

    async def get_new_nft_id(self):
        for contract_id, contract_address in random.choice(list(STARKSTARS_COUNTACTS.items())):
            if contract_id in STARKSTARS_NFT_CONTRACTS or STARKSTARS_NFT_CONTRACTS == 0:
                nft_contract = await self.client.get_contract(contract_address=contract_address)
                if not (await nft_contract.functions["balance_of"].call(self.client.address))[0]:
                    return contract_id
        raise RuntimeError('All StarkStars NFT have been minted')

    @repeater
    @gas_checker
    async def mint(self):
        await self.client.initialize_account()

        eth_contract = TOKENS_PER_CHAIN[self.client.network.name]["ETH"]

        contact_id = await self.get_new_nft_id()

        nft_contract = await self.client.get_contract(contract_address=STARKSTARS_COUNTACTS[contact_id])

        self.logger_msg(*self.client.acc_info, msg=f"Mint StarkStars#00{contact_id:0>2} NFT")

        mint_price = (await nft_contract.functions["get_price"].call())[0]

        approve_call = self.client.get_approve_call(eth_contract, nft_contract.address, mint_price)

        mint_call = nft_contract.functions["mint"].prepare()

        return await self.client.send_transaction(approve_call, mint_call)

