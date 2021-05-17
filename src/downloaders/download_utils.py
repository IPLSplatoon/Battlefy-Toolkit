import logging
from typing import Union, List, Optional, Dict

import requests


def fetch_json(address, headers: Optional[Dict[str, str]] = None, error_handling: str = 'log') -> Union[None, dict, List[dict]]:
    """Fetch JSON from an address and returns it.
    Set error_handling to 'raise' to raise an exception on unsuccessful calls.
    Set to log to log the occurrence and return None.
    Otherwise returns None and discards.
    """
    logging.info(f'Getting from {address}')

    response = requests.get(address, headers=headers)
    if response.status_code != 200:
        if error_handling == 'raise':
            raise RuntimeError(f"Bad response from {address} ({response.status_code})")
        else:
            if error_handling == 'log':
                logging.info(f"{response.status_code} response from {address}.")
            return None

    return response.json()
