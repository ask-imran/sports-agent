import sys
import os
# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from models.models import Team, Player, Match
from datetime import datetime

# Mock Players
players_team_1 = [
    Player(
        id=1,
        name="Lionel Messi",
        position="Forward",
        goals=25,
        assists=12,
        yellow_cards=2,
        red_cards=0,
        matches_played=20,
    ),
    Player(
        id=2,
        name="Sergio Busquets",
        position="Midfielder",
        goals=2,
        assists=8,
        yellow_cards=5,
        red_cards=0,
        matches_played=18,
    ),
    Player(
        id=3,
        name="Gerard Pique",
        position="Defender",
        goals=1,
        assists=2,
        yellow_cards=3,
        red_cards=1,
        matches_played=19,
    ),
]

players_team_2 = [
    Player(
        id=4,
        name="Cristiano Ronaldo",
        position="Forward",
        goals=22,
        assists=5,
        yellow_cards=3,
        red_cards=0,
        matches_played=19,
    ),
    Player(
        id=5,
        name="Luka Modric",
        position="Midfielder",
        goals=4,
        assists=10,
        yellow_cards=2,
        red_cards=0,
        matches_played=20,
    ),
    Player(
        id=6,
        name="Sergio Ramos",
        position="Defender",
        goals=3,
        assists=1,
        yellow_cards=8,
        red_cards=2,
        matches_played=17,
    ),
]

# Mock Teams
TEAMS = {
    1: Team(
        id=1,
        name="Barcelona FC",
        league="La Liga",
        wins=15,
        losses=3,
        draws=2,
        goals_for=45,
        goals_against=18,
        players=players_team_1,
    ),
    2: Team(
        id=2,
        name="Real Madrid",
        league="La Liga",
        wins=14,
        losses=4,
        draws=2,
        goals_for=42,
        goals_against=22,
        players=players_team_2,
    ),
}

# Mock Matches
MATCHES = {
    1: Match(
        id=1,
        home_team_id=1,
        away_team_id=2,
        date=datetime(2024, 12, 15, 20, 0),
        status="upcoming",
    )
}
