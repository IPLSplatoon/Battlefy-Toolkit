from datetime import datetime
from typing import List, Optional

# Generated from https://jsonformatter.org/json-to-python


class Contact:
    def __init__(self, details: str, type: str):
        self.details = details
        self.type = type


class CustomField:
    def __init__(self, name: str, public: bool, id: str):
        self.name = name
        self.public = public
        self.id = id


class EmailsSent:
    def __init__(self, one_day: bool, now: bool):
        self.one_day = one_day
        self.now = now


class Game:
    def __init__(self, id: str, name: str, icon_url: str, image_url: str, abbreviation: str, background_url: str,
                 created_at: datetime, updated_at: datetime, slug: str, default_players_per_team: int,
                 aliases: List[str], cloud_search_document_hash: str,
                 cloud_search_document_last_generated: datetime):
        self.id = id
        self.name = name
        self.icon_url = icon_url
        self.image_url = image_url
        self.abbreviation = abbreviation
        self.background_url = background_url
        self.created_at = created_at
        self.updated_at = updated_at
        self.slug = slug
        self.default_players_per_team = default_players_per_team
        self.aliases = aliases
        self.cloud_search_document_hash = cloud_search_document_hash
        self.cloud_search_document_last_generated = cloud_search_document_last_generated


class GameAttributes:
    pass


class Features:
    def __init__(self, charge_entry_fee: bool, experience: bool,
                 recommended_surface: bool, can_recommend_multiple_tournaments: bool, ladder: bool):
        self.charge_entry_fee = charge_entry_fee
        self.experience = experience
        self.recommended_surface = recommended_surface
        self.can_recommend_multiple_tournaments = can_recommend_multiple_tournaments
        self.ladder = ladder


class Owner:
    def __init__(self, id: str, timezone: str):
        self.id = id
        self.timezone = timezone


class Organization:
    def __init__(self, id: str, name: str, logo_url: str, banner_url: str, slug: str, owner_id: str, 
                 features: Features, followers: int, owner: Owner):
        self.id = id
        self.name = name
        self.logo_url = logo_url
        self.banner_url = banner_url
        self.slug = slug
        self.owner_id = owner_id
        self.features = features
        self.followers = followers
        self.owner = owner


class Rules:
    def __init__(self, complete: str, critical: str):
        self.complete = complete
        self.critical = critical


class Series:
    def __init__(self, round_num: int, num_games: int, round_type: Optional[str], round_text: Optional[str]):
        self.round = round_num
        self.num_games = num_games
        self.round_type = round_type
        self.round_text = round_text


class Bracket:
    def __init__(self, type: str, groups_count: Optional[int], series_style: str, series: List[Series],
                 has_third_place_match: bool, teams_count: int, teams_per_group: Optional[int],
                 current_round_number: Optional[int], style: Optional[str], rounds_count: Optional[int]):
        self.type = type
        self.groups_count = groups_count
        self.series_style = series_style
        self.series = series
        self.has_third_place_match = has_third_place_match
        self.teams_count = teams_count
        self.teams_per_group = teams_per_group
        self.current_round_number = current_round_number
        self.style = style
        self.rounds_count = rounds_count


class Stage:
    def __init__(self, id: str, name: str, start_time: datetime, bracket: Bracket, has_started: bool,
                 has_match_checkin: Optional[bool], has_checkin_timer: Optional[bool]):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.bracket = bracket
        self.has_started = has_started
        self.has_match_checkin = has_match_checkin
        self.has_checkin_timer = has_checkin_timer


class Stream:
    def __init__(self, id: str, provider: str, name: str, link: str, created_at: datetime, updated_at: datetime):
        self.id = id
        self.provider = provider
        self.name = name
        self.link = link
        self.created_at = created_at
        self.updated_at = updated_at


class TournamentInfo:
    def __init__(self, id: str, start_time: datetime, custom_fields: List[CustomField], players_per_team: int,
                 name: str, banner_url: str, contact: Contact, type: str, has_max_players: bool, max_players: int,
                 paid: int, has_registration_cap: bool, check_in_required: bool, check_in_starts: int,
                 user_can_report: bool, require_screenshot_for_score_reporting: bool, is_published: bool,
                 has_password: bool, about: str, schedule: str, prizes: str, game_name: str, is_featured: bool,
                 is_public: bool, is_suspended: bool, is_roster_locked: bool, registration_enabled: bool,
                 game_attributes: GameAttributes, emails_sent: EmailsSent, created_at: datetime, updated_at: datetime,
                 check_in_start_time: datetime, slug: str, organization_id: str, game_id: str, stage_i_ds: List[str],
                 stream_i_ds: List[str], rules: Rules, contact_details: str, service_fee_percent: int,
                 has_finished_seeding: bool, cloud_search_document_hash: str,
                 cloud_search_document_last_generated: datetime, stages: List[Stage], organization: Organization,
                 game: Game, streams: List[Stream]):
        self.id = id
        self.start_time = start_time
        self.custom_fields = custom_fields
        self.players_per_team = players_per_team
        self.name = name
        self.banner_url = banner_url
        self.contact = contact
        self.type = type
        self.has_max_players = has_max_players
        self.max_players = max_players
        self.paid = paid
        self.has_registration_cap = has_registration_cap
        self.check_in_required = check_in_required
        self.check_in_starts = check_in_starts
        self.user_can_report = user_can_report
        self.require_screenshot_for_score_reporting = require_screenshot_for_score_reporting
        self.is_published = is_published
        self.has_password = has_password
        self.about = about
        self.schedule = schedule
        self.prizes = prizes
        self.game_name = game_name
        self.is_featured = is_featured
        self.is_public = is_public
        self.is_suspended = is_suspended
        self.is_roster_locked = is_roster_locked
        self.registration_enabled = registration_enabled
        self.game_attributes = game_attributes
        self.emails_sent = emails_sent
        self.created_at = created_at
        self.updated_at = updated_at
        self.check_in_start_time = check_in_start_time
        self.slug = slug
        self.organization_id = organization_id
        self.game_id = game_id
        self.stage_i_ds = stage_i_ds
        self.stream_i_ds = stream_i_ds
        self.rules = rules
        self.contact_details = contact_details
        self.service_fee_percent = service_fee_percent
        self.has_finished_seeding = has_finished_seeding
        self.cloud_search_document_hash = cloud_search_document_hash
        self.cloud_search_document_last_generated = cloud_search_document_last_generated
        self.stages = stages
        self.organization = organization
        self.game = game
        self.streams = streams
