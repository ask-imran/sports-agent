from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Player(BaseModel):
    id: int
    name: str
    position: str  # "batsman", "bowler", "all-rounder", "wicket-keeper"

    # Batting statistics
    runs_scored: int
    highest_score: int
    batting_average: float
    strike_rate: float
    fifties: int
    hundreds: int
    ducks: int
    not_outs: int

    # Bowling statistics
    wickets_taken: int
    bowling_average: float
    economy_rate: float
    best_bowling_figures: str  # e.g., "5/23"

    # General statistics
    matches_played: int
    catches: int
    stumpings: int  # for wicket-keepers


class Team(BaseModel):
    id: int
    name: str
    league: str
    wins: int
    losses: int
    draws: int
    no_results: int  # rain/weather cancellations
    runs_scored: int
    runs_conceded: int
    players: List[Player]


class Match(BaseModel):
    id: int
    home_team_id: int
    away_team_id: int
    date: datetime
    home_score: Optional[str] = None  # e.g., "280/8 (50 overs)"
    away_score: Optional[str] = None  # e.g., "245 all out (48.3 overs)"
    match_format: str  # "Test", "ODI", "T20"
    venue: str
    status: str  # "upcoming", "in_progress", "completed", "abandoned"


class MatchAnalysis(BaseModel):
    winner: str
    win_probability: float
    reasoning: str
    key_factors: List[str]
    home_team_strength: float
    away_team_strength: float
