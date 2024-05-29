import logging

from .connection import Connection
from .const import *
from .models import Contract, Consumption, LastInvoice

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class Goldenergy:
    def __init__(self, session):
        self._connection = Connection(session)
        self._contract = None
        self._last_consumption = None

    async def login(self, code, password):
        _LOGGER.debug("Goldenergy API Login")
        url = ENDPOINT + LOGIN_PATH

        data = {
            CODE_PARAM: code,
            PWD_PARAM: password
        }

        res = await self._connection.api_request(url, method="post", data=data)
        if res is not None:
            try:
                self._connection.set_token(res["result"]["token"])
                return True
            except:
                return False
        return False

    async def get_contract(self, contract_number: str) -> Contract:
        _LOGGER.debug("Goldenergy API Contract")

        url = ENDPOINT + CONTRACT_LIST_PATH

        contract_api_response = await self._connection.api_request(url, params={"ContractNo": contract_number})
        contract = contract_api_response["result"]

        self._contract = Contract.from_dict(contract)
        return self._contract

    async def get_last_invoice(self, contract_number: str) -> LastInvoice:
        _LOGGER.debug("Goldenergy API Contract")

        if (self._contract is not None) and (self._contract.contractNo == contract_number):
            return self._contract.lastInvoice

        url = ENDPOINT + CONTRACT_LIST_PATH

        contract_api_response = await self._connection.api_request(url, params={"ContractNo": contract_number})
        contract = contract_api_response["result"]

        self._contract = Contract.from_dict(contract)
        return self._contract.lastInvoice

    async def get_last_consumption(self, contract_no: str) -> [Consumption]:
        _LOGGER.debug("Goldenergy API Consumptions")

        url = ENDPOINT + CONSUMPTIONS_PATH

        consumptions_api_response = await self._connection.api_request(
            url,
            params={"ContractNo": contract_no}
        )
        consumption = consumptions_api_response["result"]["items"][0]

        self._last_consumption = Consumption.from_dict(consumption)
        return self._last_consumption
