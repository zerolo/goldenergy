# Goldenergy API

## Installation

    pip install goldenergy

## Usage
```python
import asyncio
import aiohttp
from src.goldenergy import Goldenergy


async def main():
    session = aiohttp.ClientSession()

    goldenergy = Goldenergy(session=session, code="<NIF>", password="<PASSWORD>")
    print("LOGIN: ", await goldenergy.login())

    print("CONTRACT: ", await goldenergy.get_contract("<CONTRACT_NUMBER>"))

    print("LATEST CONTRACT: ", await goldenergy.get_latest_contract())

    print("LAST INVOICE: ", await goldenergy.get_last_invoice("<CONTRACT_NUMBER>"))

    print("CONSUMPTIONS: ", await goldenergy.get_last_consumption("<CONTRACT_NUMBER>"))

    await session.close()


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())

```

## Tests
Make sure pytest asyncio is installed
```bash
$ pip install pytest-asyncio
```
Execute the tests
```bash
$ pytest tests/
```