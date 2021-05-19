from typing import Optional, List

from battlefy_toolkit.objects import TournamentInfo, TournamentTeam
from battlefy_toolkit.objects import TournamentStage


class Tournament:
    def __init__(self, tournament_slug: str):
        """Constructor for Tournament"""
        self.slug = tournament_slug
        self.info: Optional[TournamentInfo] = None
        self.stages: Optional[List[TournamentStage]] = None
        self.teams: Optional[List[TournamentTeam]] = None
