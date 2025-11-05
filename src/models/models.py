from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Player(BaseModel):
    id: int
    name: str
    position: str
    goals: int
    assists: int
    yellow_cards: int
    red_cards: int
    matches_played: int


class Team(BaseModel):
    id: int
    name: str
    league: str
    wins: int
    losses: int
    draws: int
    goals_for: int
    goals_against: int
    players: List[Player]


class Match(BaseModel):
    id: int
    home_team_id: int
    away_team_id: int
    date: datetime
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    status: str  # "upcoming", "completed"


class MatchAnalysis(BaseModel):
    winner: str
    win_probability: float
    reasoning: str
    key_factors: List[str]
    home_team_strength: float
    away_team_strength: float
