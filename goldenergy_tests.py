import unittest
import pytest
import aiohttp
from unittest.mock import MagicMock
from goldenergy import Goldenergy


def create_mock(status_code, get_json_response, post_json_response):
    mock = aiohttp.ClientSession()
    mock.post = MagicMock()
    mock.post.return_value.__aenter__.return_value.status = status_code
    mock.post.return_value.__aenter__.return_value.content_type = "application/json"
    mock.post.return_value.__aenter__.return_value.json.return_value = post_json_response

    mock.get = MagicMock()
    mock.get.return_value.__aenter__.return_value.status = status_code
    mock.get.return_value.__aenter__.return_value.content_type = "application/json"
    mock.get.return_value.__aenter__.return_value.json.return_value = get_json_response

    return mock


@pytest.fixture
def setup_mocks():
    token_response = {
        "result": {
            "token": "my_token"
        }
    }

    token_no_response = {
        "title": "Unauthorized"
    }

    contract_response = {
        "result": {
            "contractNo": "111",
            "status": 1,
            "initDate": "2024-03-28T00:00:00",
            "endDate": None,
            "nextReadingDate": "2024-05-25T00:00:00",
            "paymentOwner": {
                "customerNo": "222",
                "name": "name",
                "nif": "123456789",
                "phone": None,
                "mobile": "+351123456789",
                "email": "mail@GMAIL.COM",
                "isLastPaymentOwner": "true"
            },
            "contractOwner": {
                "customerNo": "222",
                "name": "name",
                "nif": "123456789",
                "phone": None,
                "mobile": "+351123456789",
                "email": "mail@GMAIL.COM",
                "isLastPaymentOwner": "true"
            },
            "electronicInvoice": {
                "email": "mail@GMAIL.COM",
                "activationDate": "2024-03-26T00:00:00",
                "active": "true"
            },
            "directDebit": {
                "activationDate": "2024-03-26T00:00:00",
                "iban": "PT50123456789",
                "adc": "12345678",
                "maximumLimit": None
            },
            "gas": {
                "energyType": 0,
                "cui": "PT123456789",
                "escalao": "1",
                "status": 1,
                "meter": {
                    "meterNo": "M1",
                    "serialNo": "123456789",
                    "smartMeter": "false"
                },
            },
            "electricity": {
                "energyType": 1,
                "cpe": "PT123456789",
                "power": "4,6 kVA",
                "tariffType": 1,
                "selfConsumption": "false",
                "status": 1,
                "meter": {
                    "meterNo": "M2",
                    "serialNo": "123456789",
                    "smartMeter": "true"
                }
            },
            "billingAddress": {
                "streetName": "street",
                "number": "111",
                "duplicator": "A",
                "fraction": "1 A",
                "postCode": "1111-111",
                "city": "city"
            },
            "consumptionPointAddress": {
                "streetName": "street",
                "number": "111",
                "duplicator": "A",
                "fraction": "1 A",
                "postCode": "1111-111",
                "city": "city"
            },
            "alias": "Luz e Gas",
            "mgmVoucherCode": "MGM123456789",
            "electricityProductList": [
                {
                    "energyType": 1,
                    "power": "4,6 kVA",
                    "tariffType": 1,
                    "initDate": "2024-03-27T00:00:00",
                    "endDate": None
                }
            ],
            "gasProductList": [
                {
                    "energyType": 0,
                    "escalao": "1",
                    "initDate": "2024-03-26T00:00:00",
                    "endDate": None
                }
            ],
            "lastInvoice": {
                "entryNo": 123456789,
                "customerNo": "222",
                "contractNo": "111",
                "dueDate": "2024-05-21T00:00:00",
                "mbReference": None,
                "charged": "true",
                "chargedDate": "2024-05-21T00:00:00",
                "amount": 61.75,
                "remainingAmount": 0,
                "billingMethodDescription": "DÉBITO DIRETO",
                "documentNo": "123456789",
                "postingDate": "2024-04-28T00:00:00",
                "billingPeriodInitDate": "2024-03-26T00:00:00",
                "billingPeriodEndDate": "2024-04-25T00:00:00"
            },
            "paymentOwnerUpdateList": [
                {
                    "initDate": "2024-03-26T00:00:00",
                    "endDate": None,
                    "customerNo": "111",
                    "name": "name",
                    "nif": "123456789"
                }
            ],
            "balanceAmount": 0
        }
    }

    last_consumption_result = {
        "result": {
            "items": [
                {
                    "date": "2024-03-01T00:00:00",
                    "energies": [
                        {
                            "energyType": 0,
                            "meters": [
                                {
                                    "meter": {
                                        "meterNo": "123456789",
                                        "serialNo": "123456789",
                                        "totalRecords": 0,
                                        "digits": 0,
                                        "initDate": None,
                                        "endDate": None,
                                        "recordTypes": [
                                            0
                                        ],
                                        "smartMeter": "false"
                                    },
                                    "realM3": 10,
                                    "estimatedM3": 0,
                                    "realKWh": 112,
                                    "estimatedKWH": 0
                                }
                            ]
                        },
                        {
                            "energyType": 1,
                            "meters": [
                                {
                                    "meter": {
                                        "meterNo": "987654321",
                                        "serialNo": "987654321",
                                        "totalRecords": 3,
                                        "digits": 0,
                                        "initDate": None,
                                        "endDate": None,
                                        "recordTypes": [
                                            2,
                                            4,
                                            5
                                        ],
                                        "smartMeter": None
                                    },
                                    "realM3": None,
                                    "estimatedM3": None,
                                    "realKWh": 122,
                                    "estimatedKWH": 0
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }

    mock_post_get_contract = create_mock(200, contract_response, token_response)
    mock_post_failure = create_mock(200, contract_response, token_no_response)
    mock_post_get_last_consumption = create_mock(200, last_consumption_result, token_response)

    yield {
        "mock_post_get_contract": mock_post_get_contract,
        "post_failure": mock_post_failure,
        "mock_post_get_last_consumption": mock_post_get_last_consumption
    }


@pytest.mark.asyncio
async def test_login_success(setup_mocks):
    mock = setup_mocks.get("mock_post_get_contract")

    goldenergy = Goldenergy(mock)

    response = await goldenergy.login("111", "222")
    assert response

    await mock.close()


@pytest.mark.asyncio
async def test_login_failed(setup_mocks):
    mock = setup_mocks.get("post_failure")

    goldenergy = Goldenergy(mock)

    response = await goldenergy.login("", "")
    assert not response

    await mock.close()


@pytest.mark.asyncio
async def test_get_contract_success(setup_mocks):
    mock = setup_mocks.get("mock_post_get_contract")

    goldenergy = Goldenergy(mock)

    response = await goldenergy.login("111", "222")
    assert response

    contract = await goldenergy.get_contract("111")
    assert contract.contractNo == "111"

    await mock.close()


@pytest.mark.asyncio
async def test_get_last_invoice_success(setup_mocks):
    mock = setup_mocks.get("mock_post_get_contract")

    goldenergy = Goldenergy(mock)

    response = await goldenergy.login("111", "222")
    assert response

    last_invoice = await goldenergy.get_last_invoice("111")
    assert last_invoice.contractNo == "111"
    assert last_invoice.amount == 61.75

    await mock.close()


@pytest.mark.asyncio
async def test_get_last_consumptions_success(setup_mocks):
    mock = setup_mocks.get("mock_post_get_last_consumption")

    goldenergy = Goldenergy(mock)

    response = await goldenergy.login("111", "222")
    assert response

    last_consumptions = await goldenergy.get_last_consumption("111")
    assert last_consumptions[0].meter.meterNo == "123456789"
    assert last_consumptions[0].energy_type == "GAS"
    assert last_consumptions[1].meter.meterNo == "987654321"
    assert last_consumptions[1].energy_type == "ELECTRICITY"

    await mock.close()


if __name__ == '__main__':
    unittest.main()
