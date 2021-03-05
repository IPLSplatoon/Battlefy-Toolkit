from typing import List
from datetime import datetime

# Generated from https://jsonformatter.org/json-to-python


class CustomField:
    id: str
    value: str

    def __init__(self, id: str, value: str):
        self.id = id
        self.value = value


class Team:
    def __init__(self, id: str, name: str, pending_team_id: str, persistent_team_id: str, tournament_id: str, 
                 user_id: str, custom_fields: List[CustomField], owner_id: str, created_at: datetime, 
                 player_ids: List[str], captain_id: str):
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


class Standings:
    def __init__(self, id: str, stage_id: str, team_id: str, round_number: int, wins: int, losses: int, ties: int, 
                 tie_break_wins: int, tie_break_lost_rounds: List[int], opponents: List[str], 
                 game_wins: int, game_losses: int, points: int, match_win_percentage: float, game_win_percentage: float, 
                 created_at: datetime, updated_at: datetime, disqualified: bool, t1: int, t3: int, 
                 opponents_match_win_percentage: float, t2: int, opponents_opponents_match_win_percentage: float, 
                 team: Team):
        self.id = id
        self.stage_id = stage_id
        self.team_id = team_id
        self.round_number = round_number
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.tie_break_wins = tie_break_wins
        self.tie_break_lost_rounds = tie_break_lost_rounds
        self.opponents = opponents
        self.game_wins = game_wins
        self.game_losses = game_losses
        self.points = points
        self.match_win_percentage = match_win_percentage
        self.game_win_percentage = game_win_percentage
        self.created_at = created_at
        self.updated_at = updated_at
        self.disqualified = disqualified
        self.t1 = t1
        self.t3 = t3
        self.opponents_match_win_percentage = opponents_match_win_percentage
        self.t2 = t2
        self.opponents_opponents_match_win_percentage = opponents_opponents_match_win_percentage
        self.team = team
