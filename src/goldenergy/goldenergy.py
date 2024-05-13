import logging
import aiohttp

from .const import ENDPOINT

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class Goldenergy:

    def __init__(self):
        self._example = "example"

    async def example_public(self):
        return True
    
