from typing import List, Optional
from datetime import datetime

# Generated from https://jsonformatter.org/json-to-python


class Series:
    def __init__(self, round_num: int, num_games: int):
        self.round = round_num
        self.num_games = num_games


class Bracket:
    def __init__(self, tiebreaker_method: str, series_style: str, series: List[Series], type: str, rounds_count: int,
                 teams_count: int, has_third_place_match: bool, current_round_number: int):
        self.tiebreaker_method = tiebreaker_method
        self.series_style = series_style
        self.series = series
        self.type = type
        self.rounds_count = rounds_count
        self.teams_count = teams_count
        self.has_third_place_match = has_third_place_match
        self.current_round_number = current_round_number


class CustomField:
    def __init__(self, id: str, value: str):
        self.id = id
        self.value = value


class Header:
    def __init__(self, url: str):
        self.url = url


class PersistentTeam:
    def __init__(self, id: str, name: str, logo: Header, header: Header, sponsor: Header, logo_url: str,
                 short_description: str, banner_url: str, sponsor_banner_url: str,
                 created_at: datetime, updated_at: datetime, team_ids: List[str], game_id: str,
                 persistent_player_ids: List[str], persistent_captain_id: str, pending_player_ids: List[str],
                 owner_id: str, deleted_at: Optional[datetime]):
        self.id = id
        self.name = name
        self.logo = logo
        self.header = header
        self.sponsor = sponsor
        self.logo_url = logo_url
        self.short_description = short_description
        self.banner_url = banner_url
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


class Battlenet:
    def __init__(self, account_id: int, battletag: str):
        self.account_id = account_id
        self.battletag = battletag


class Twitter:
    def __init__(self, screen_name: str, account_id: str):
        self.screen_name = screen_name
        self.account_id = account_id


class PurpleAccounts:
    def __init__(self, battlenet: Optional[Battlenet], twitter: Optional[Twitter], twitch: Optional[str]):
        self.battlenet = battlenet
        self.twitter = twitter
        self.twitch = twitch


class EmailSubscriptionsClass:
    pass


class Equipment:
    def __init__(self, face: str, body: Optional[str], head: Optional[str]):
        self.face = face
        self.body = body
        self.head = head


class Features:
    def __init__(self, onboarded_store: Optional[bool], open_store: Optional[bool],
                 completed_store_exit_survey: Optional[bool], new_join_info_bar: Optional[bool]):
        self.onboarded_store = onboarded_store
        self.open_store = open_store
        self.completed_store_exit_survey = completed_store_exit_survey
        self.new_join_info_bar = new_join_info_bar


class PurpleUser:
    def __init__(self, id: str, timezone: str, source: Optional[str], auth0_user_id: str,
                 username: str, is_verified: bool, email_subscriptions: EmailSubscriptionsClass,
                 created_at: datetime, updated_at: datetime, slug: str, equipment: Optional[Equipment],
                 features: Features, valid_email: bool, experience_points: int, bg_url: Optional[str],
                 avatar_url: Optional[str], accounts: Optional[PurpleAccounts], has_seen_vgl_ad_at: Optional[datetime],
                 country_code: Optional[str], deactivated_at: Optional[datetime],
                 normalized_username: Optional[str], deleted_at: Optional[datetime],
                 has_seen_ncsa_ad_at: Optional[datetime]):
        self.id = id
        self.timezone = timezone
        self.source = source
        self.auth0_user_id = auth0_user_id
        self.username = username
        self.is_verified = is_verified
        self.email_subscriptions = email_subscriptions
        self.created_at = created_at
        self.updated_at = updated_at
        self.slug = slug
        self.equipment = equipment
        self.features = features
        self.valid_email = valid_email
        self.experience_points = experience_points
        self.bg_url = bg_url
        self.avatar_url = avatar_url
        self.accounts = accounts
        self.has_seen_vgl_ad_at = has_seen_vgl_ad_at
        self.country_code = country_code
        self.deactivated_at = deactivated_at
        self.normalized_username = normalized_username
        self.deleted_at = deleted_at
        self.has_seen_ncsa_ad_at = has_seen_ncsa_ad_at


class PurplePlayer:
    def __init__(self, id: str, on_team: bool, is_free_agent: bool, be_captain: bool, in_game_name: str,
                 game_id: str, persistent_player_id: Optional[str], user_id: Optional[str],
                 owner_id: str, created_at: datetime, updated_at: datetime, custom_fields: List[CustomField],
                 organization_id: str, tournament_id: str, user: Optional[PurpleUser]):
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
        self.custom_fields = custom_fields
        self.organization_id = organization_id
        self.tournament_id = tournament_id
        self.user = user


class BottomTeam:
    def __init__(self, id: str, name: str, pending_team_id: str, persistent_team_id: str,
                 tournament_id: str, user_id: str, custom_fields: List[CustomField],
                 owner_id: str, created_at: datetime, player_ids: List[str], captain_id: str,
                 players: List[PurplePlayer], persistent_team: PersistentTeam):
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
        self.players = players
        self.persistent_team = persistent_team


class MatchBottom:
    def __init__(self, seed_number: Optional[int], team_id: str, winner: bool, disqualified: bool,
                 score: int, team: BottomTeam):
        self.seed_number = seed_number
        self.team_id = team_id
        self.winner = winner
        self.disqualified = disqualified
        self.score = score
        self.team = team


class ScreenshotsTop:
    def __init__(self, game_1: List[str], game_2: List[str]):
        self.game_1 = game_1
        self.game_2 = game_2


class Screenshots:
    def __init__(self, top: ScreenshotsTop, bottom: EmailSubscriptionsClass):
        self.top = top
        self.bottom = bottom


class TopClass:
    def __init__(self, winner: bool):
        self.winner = winner


class Stats:
    def __init__(self, top: TopClass, bottom: TopClass, is_complete: bool, game_round_results: Optional[List[str]]):
        self.top = top
        self.bottom = bottom
        self.is_complete = is_complete
        self.game_round_results = game_round_results


class Stat:
    def __init__(self, match_id: str, game_id: str, tournament_id: str, stage_id: str, game_number: int,
                 stats: Stats, created_at: datetime, id: str):
        self.match_id = match_id
        self.game_id = game_id
        self.tournament_id = tournament_id
        self.stage_id = stage_id
        self.game_number = game_number
        self.stats = stats
        self.created_at = created_at
        self.id = id


class FluffyAccounts:
    def __init__(self, twitter: Optional[Twitter], twitch: Optional[str]):
        self.twitter = twitter
        self.twitch = twitch


class FluffyUser:
    def __init__(self, id: str, timezone: str, source: Optional[str], auth0_user_id: str, username: str,
                 is_verified: bool, email_subscriptions: EmailSubscriptionsClass, created_at: datetime,
                 updated_at: datetime, slug: str, equipment: Optional[Equipment], features: Features,
                 experience_points: int, valid_email: bool, avatar_url: Optional[str], bg_url: Optional[str],
                 accounts: Optional[FluffyAccounts], deactivated_at: Optional[datetime],
                 normalized_username: Optional[str], deleted_at: Optional[datetime],
                 has_seen_vgl_ad_at: Optional[datetime], has_seen_ncsa_ad_at: Optional[datetime],
                 country_code: Optional[str]):
        self.id = id
        self.timezone = timezone
        self.source = source
        self.auth0_user_id = auth0_user_id
        self.username = username
        self.is_verified = is_verified
        self.email_subscriptions = email_subscriptions
        self.created_at = created_at
        self.updated_at = updated_at
        self.slug = slug
        self.equipment = equipment
        self.features = features
        self.experience_points = experience_points
        self.valid_email = valid_email
        self.avatar_url = avatar_url
        self.bg_url = bg_url
        self.accounts = accounts
        self.deactivated_at = deactivated_at
        self.normalized_username = normalized_username
        self.deleted_at = deleted_at
        self.has_seen_vgl_ad_at = has_seen_vgl_ad_at
        self.has_seen_ncsa_ad_at = has_seen_ncsa_ad_at
        self.country_code = country_code


class FluffyPlayer:
    def __init__(self, id: str, on_team: bool, is_free_agent: bool, be_captain: bool, in_game_name: str,
                 game_id: str, persistent_player_id: Optional[str], user_id: Optional[str], owner_id: str,
                 created_at: datetime, updated_at: datetime, custom_fields: List[CustomField],
                 organization_id: str, tournament_id: str, user: Optional[FluffyUser]):
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
        self.custom_fields = custom_fields
        self.organization_id = organization_id
        self.tournament_id = tournament_id
        self.user = user


class TopTeam:
    def __init__(self, id: str, name: str, pending_team_id: str, persistent_team_id: str, tournament_id: str,
                 user_id: str, custom_fields: List[CustomField], owner_id: str, created_at: datetime,
                 player_ids: List[str], captain_id: str, players: List[FluffyPlayer], persistent_team: PersistentTeam):
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
        self.players = players
        self.persistent_team = persistent_team


class MatchTop:
    def __init__(self, seed_number: Optional[int], team_id: str, winner: bool, disqualified: bool,
                 score: int, team: TopTeam):
        self.seed_number = seed_number
        self.team_id = team_id
        self.winner = winner
        self.disqualified = disqualified
        self.score = score
        self.team = team


class Match:
    def __init__(self, id: str, match_number: int, round_number: int, top: MatchTop, bottom: MatchBottom,
                 is_bye: bool, is_complete: bool, stage_id: str, created_at: datetime, updated_at: datetime,
                 stats: Optional[List[Stat]], in_consolation_bracket: bool, double_loss: bool, is_tie: Optional[bool],
                 is_double_loss: Optional[bool], completed_at: datetime, screenshots: Optional[Screenshots],
                 is_marked_live: Optional[bool]):
        self.id = id
        self.match_number = match_number
        self.round_number = round_number
        self.top = top
        self.bottom = bottom
        self.is_bye = is_bye
        self.is_complete = is_complete
        self.stage_id = stage_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.stats = stats
        self.in_consolation_bracket = in_consolation_bracket
        self.double_loss = double_loss
        self.is_tie = is_tie
        self.is_double_loss = is_double_loss
        self.completed_at = completed_at
        self.screenshots = screenshots
        self.is_marked_live = is_marked_live


class TournamentStage:
    def __init__(self, id: str, name: str, start_time: datetime, bracket: Bracket, created_at: datetime,
                 has_started: bool, updated_at: datetime, standing_ids: List[str], team_ids: List[str],
                 group_ids: List[str], match_ids: List[str], started_at: datetime,
                 matches: List[Match], groups: List[str]):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.bracket = bracket
        self.created_at = created_at
        self.has_started = has_started
        self.updated_at = updated_at
        self.standing_ids = standing_ids
        self.team_ids = team_ids
        self.group_ids = group_ids
        self.match_ids = match_ids
        self.started_at = started_at
        self.matches = matches
        self.groups = groups
