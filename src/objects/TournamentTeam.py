from typing import Optional, List, Any
from datetime import datetime

# Generated from https://jsonformatter.org/json-to-python


class Equipment:
    def __init__(self, face: str, head: Optional[str], body: Optional[str]):
        self.face = face
        self.head = head
        self.body = body


class Captain:
    def __init__(self, id: str, on_team: bool, is_free_agent: bool, be_captain: bool, in_game_name: str, 
                 game_id: str, persistent_player_id: Optional[str], user_id: Optional[str], owner_id: str, 
                 created_at: datetime, updated_at: datetime, tournament_id: str, organization_id: str, 
                 user_slug: Optional[str], equipment: Optional[Equipment], username: Optional[str], 
                 avatar_url: Optional[str], invite_referral: Optional[str]):
        self.id = id
        self.on_team = on_team
        self.is_free_agent = is_free_agent
        self.be_captain = be_captain
        self.in_game_name = in_game_name
        self.game_id = game_id
        self.persistent_player_id = persistent_player_id
        self.user_id = user_id
        self.owner_id = owner_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.tournament_id = tournament_id
        self.organization_id = organization_id
        self.user_slug = user_slug
        self.equipment = equipment
        self.username = username
        self.avatar_url = avatar_url
        self.invite_referral = invite_referral


class CustomField:
    def __init__(self, id: str, value: str):
        self.id = id
        self.value = value


class Header:
    def __init__(self, url: str):
        self.url = url


class PersistentTeam:
    def __init__(self, id: str, name: str, logo: Header, header: Header, sponsor: Header, short_description: str, 
                 banner_url: str, logo_url: str, sponsor_banner_url: str, created_at: datetime, updated_at: datetime, 
                 team_ids: List[Any], game_id: str, persistent_player_ids: List[str], persistent_captain_id: str, 
                 pending_player_ids: List[Any], owner_id: str, deleted_at: Optional[datetime]):
        self.id = id
        self.name = name
        self.logo = logo
        self.header = header
        self.sponsor = sponsor
        self.short_description = short_description
        self.banner_url = banner_url
        self.logo_url = logo_url
        self.sponsor_banner_url = sponsor_banner_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.team_ids = team_ids
        self.game_id = game_id
        self.persistent_player_ids = persistent_player_ids
        self.persistent_captain_id = persistent_captain_id
        self.pending_player_ids = pending_player_ids
        self.owner_id = owner_id
        self.deleted_at = deleted_at


class TournamentTeam:
    def __init__(self, id: str, name: str, pending_team_id: str, persistent_team_id: str,
                 tournament_id: str, user_id: str, custom_fields: List[CustomField], owner_id: str,
                 created_at: datetime, player_ids: List[str], captain_id: str, checked_in_at: Optional[datetime],
                 captain: Captain, players: List[Captain], persistent_team: PersistentTeam):
        self.id = id
        self.name = name
        self.pending_team_id = pending_team_id
        self.persistent_team_id = persistent_team_id
        self.tournament_id = tournament_id
        self.user_id = user_id
        self.custom_fields = custom_fields
        self.owner_id = owner_id
        self.created_at = created_at
        self.player_ids = player_ids
        self.captain_id = captain_id
        self.checked_in_at = checked_in_at
        self.captain = captain
        self.players = players
        self.persistent_team = persistent_team
