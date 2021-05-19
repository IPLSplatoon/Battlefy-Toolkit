import logging
from typing import Optional

import requests

from battlefy_toolkit.downloaders.download_utils import fetch_json
from battlefy_toolkit.endpoints.addresses import ORG_ADDRESS_FORMAT, ORG_SEARCH_FORMAT

HEADERS = {
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}


def get_org(org_slug: str) -> Optional[dict]:
    """
    Fetch the org file from its slug
    :param org_slug: The org slug, e.g. inkling-performance-labs
    :return: The json or None
    """
    return fetch_json(ORG_ADDRESS_FORMAT.format(org_slug=org_slug), headers=HEADERS)


def get_tournament_ids(org_slug: str) -> Optional[list]:
    org_data = get_org(org_slug)
    if org_data:
        org_id = org_data[0]["_id"]
    else:
        logging.error(f'Not able to get the Org {org_slug}')
        return None

    tournaments = []
    page_one_old = requests.get(ORG_SEARCH_FORMAT.format(org_id=org_id, page=1), headers=HEADERS)
    pages = 0
    if page_one_old.status_code == 200:
        page_one_data = page_one_old.json()
        if "total" in page_one_data:
            pages = int(page_one_data["total"] / 10)
            if pages > 0:
                pages = pages+1
            if (page_one_data["total"] % 10) != 0:
                pages = pages+1
        if "tournaments" in page_one_data:
            for items in page_one_data["tournaments"]:
                tournaments.append(items["_id"])
    else:
        logging.error('Bad response from ' + org_slug + ", id " + org_id)
        return None

    for x in range(2, pages):
        page = requests.get(ORG_SEARCH_FORMAT.format(org_id=org_id, page=x), headers=HEADERS)
        if page.status_code == 200:
            page_data = page.json()
            if "tournaments" in page_data:
                for items in page_data["tournaments"]:
                    tournaments.append(items["_id"])

    return tournaments
