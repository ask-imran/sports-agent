from fastapi import FastAPI, HTTPException
from typing import List
from ..models.models import Team, Player, Match
from .mock_data import TEAMS, MATCHES

app = FastAPI(title="Sports Data API", version="1.0.0")


@app.get("/")
def root():
    return {"message": "Sports Data API - Week 1"}


@app.get("/teams", response_model=List[Team])
def get_all_teams():
    return list(TEAMS.values())


@app.get("/teams/{team_id}", response_model=Team)
def get_team(team_id: int):
    if team_id not in TEAMS:
        raise HTTPException(status_code=404, detail="Team not found")
    return TEAMS[team_id]


@app.get("/players", response_model=List[Player])
def get_all_players():
    all_players = []
    for team in TEAMS.values():
        all_players.extend(team.players)
    return all_players


@app.get("/matches", response_model=List[Match])
def get_all_matches():
    return list(MATCHES.values())


@app.get("/matches/{match_id}", response_model=Match)
def get_match(match_id: int):
    if match_id not in MATCHES:
        raise HTTPException(status_code=404, detail="Match not found")
    return MATCHES[match_id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
