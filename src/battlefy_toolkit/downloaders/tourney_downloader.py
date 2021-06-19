import logging
from typing import Optional, Set, List

from battlefy_toolkit.downloaders.download_utils import fetch_json
from battlefy_toolkit.downloaders.org_downloader import get_tournament_ids
from battlefy_toolkit.endpoints.addresses import TOURNAMENT_INFO_FETCH_ADDRESS_FORMAT, STAGE_INFO_FETCH_ADDRESS_FORMAT, \
    TEAMS_FETCH_ADDRESS_FORMAT, TOURNAMENT_BASIC_INFO_FETCH_ADDRESS_FORMAT
from battlefy_toolkit.org_lists.splatoon_orgs import ORG_SLUGS


def get_basic_tournament_info(tournament_id: str) -> Optional[dict]:
    return fetch_json(TOURNAMENT_BASIC_INFO_FETCH_ADDRESS_FORMAT.format(tourney_id=tournament_id))


def get_tourney_info_file(tourney_id_to_fetch: str) -> Optional[dict]:
    """
    Get the tourney contents corresponding to the given tourney id.
    This is an API call.
    :param tourney_id_to_fetch: The Battlefy id.
    :return: The tourney contents, or None.
    """
    tourney_contents = fetch_json(TOURNAMENT_INFO_FETCH_ADDRESS_FORMAT.format(tourney_id=tourney_id_to_fetch))

    if len(tourney_contents) == 0:
        logging.error(f'Nothing exists at {tourney_id_to_fetch=}.')
        return None

    if isinstance(tourney_contents, list):
        tourney_contents = tourney_contents[0]

    return tourney_contents


def get_tourney_teams_file(tourney_id_to_fetch: str) -> Optional[List[dict]]:
    teams_contents = fetch_json(TEAMS_FETCH_ADDRESS_FORMAT.format(tourney_id=tourney_id_to_fetch))

    if len(teams_contents) == 0:
        logging.error(f'Nothing exists at {tourney_id_to_fetch=}.')
        return None

    if not isinstance(teams_contents, list):
        teams_contents = [teams_contents]

    return teams_contents


def get_stage_ids_for_tourney(tourney_id_to_fetch: str) -> Set[str]:
    """"
    Returns stage ids for the specified tourney.
    This is an API call.
    """
    tourney_contents = get_tourney_info_file(tourney_id_to_fetch) or set()
    return set(tourney_contents.get('stageIDs', set()))


def get_stage_file(stage_id_to_fetch: str) -> Optional[dict]:
    """"
    Returns the stage file for specified tourney and stage id.
    This in an API call.
    """
    if not stage_id_to_fetch:
        raise ValueError(f'Expected id {stage_id_to_fetch=}')

    _stage_contents = fetch_json(STAGE_INFO_FETCH_ADDRESS_FORMAT.format(stage_id=stage_id_to_fetch))
    if len(_stage_contents) == 0:
        logging.error(f'Nothing exists at {stage_id_to_fetch=}')
        return None

    if isinstance(_stage_contents, list):
        _stage_contents = _stage_contents[0]

    return _stage_contents


def get_or_fetch_tourney_ids() -> Set[str]:
    """
    Get a set of tourney ids from the Orgs that we watch.
    This in an API call.
    """

    result = set()
    for org in ORG_SLUGS:
        tournaments = get_tournament_ids(org)
        if tournaments:
            for t in tournaments:
                tournament_info = get_tourney_info_file(t)
                if tournament_info:
                    name = tournament_info.get("gameName")
                    if name.startswith("Splatoon"):
                        result.add(t)
    return result
