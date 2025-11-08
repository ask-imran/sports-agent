from typing import Dict, Any
import httpx
from pydantic_ai import Agent, RunContext


class DataService:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url

    async def get_team(self, team_id: int) -> Dict[str, Any]:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/teams/{team_id}")
            response.raise_for_status()
            return response.json()


def register_tools(sports_agent: Agent):
    """Register tools with the sports agent."""

    @sports_agent.tool
    async def get_team_stats(
        ctx: RunContext[DataService], team_id: int
    ) -> Dict[str, Any]:
        """Get comprehensive statistics for a team including players."""
        print(f"📊 Getting team stats for Team {team_id}...")
        return await ctx.deps.get_team(team_id)

    @sports_agent.tool
    async def calculate_team_strength(
        ctx: RunContext[DataService], team_id: int
    ) -> float:
        """Calculate a team's overall strength score based on cricket statistics."""
        print(f"💪 Calculating team strength for Team {team_id}...")
        team_data = await ctx.deps.get_team(team_id)

        # Cricket-specific strength calculation
        total_games = (
            team_data["wins"]
            + team_data["losses"]
            + team_data["draws"]
            + team_data["no_results"]
        )
        if total_games == 0:
            return 0.5

        # Win rate (excluding no-results from denominator for meaningful calculation)
        meaningful_games = total_games - team_data["no_results"]
        if meaningful_games == 0:
            win_rate = 0.5
        else:
            win_rate = team_data["wins"] / meaningful_games

        # Run rate differential (runs scored vs runs conceded)
        if meaningful_games > 0:
            avg_runs_scored = team_data["runs_scored"] / meaningful_games
            avg_runs_conceded = team_data["runs_conceded"] / meaningful_games
            run_difference = avg_runs_scored - avg_runs_conceded
        else:
            run_difference = 0

        # Player quality assessment based on batting and bowling averages
        players = team_data["players"]
        if players:
            # Batting strength - higher batting averages are better
            batting_averages = [
                p["batting_average"] for p in players if p["batting_average"] > 0
            ]
            avg_batting_average = (
                sum(batting_averages) / len(batting_averages)
                if batting_averages
                else 25.0
            )

            # Bowling strength - lower bowling averages are better
            bowling_averages = [
                p["bowling_average"]
                for p in players
                if p["bowling_average"] > 0 and p["wickets_taken"] > 0
            ]
            avg_bowling_average = (
                sum(bowling_averages) / len(bowling_averages)
                if bowling_averages
                else 35.0
            )

            # Strike rates for batting aggression
            strike_rates = [p["strike_rate"] for p in players if p["strike_rate"] > 0]
            avg_strike_rate = (
                sum(strike_rates) / len(strike_rates) if strike_rates else 80.0
            )

            # Normalize batting strength (average of 40+ is excellent)
            batting_strength = min(avg_batting_average / 50.0, 1.0)

            # Normalize bowling strength (average below 25 is excellent, inverse scale)
            bowling_strength = max(0, 1.0 - (avg_bowling_average - 20.0) / 30.0)

            # Strike rate factor (90+ is aggressive, good for limited overs)
            strike_rate_factor = min(avg_strike_rate / 100.0, 1.2) * 0.8  # Cap at 0.96
        else:
            batting_strength = 0.5
            bowling_strength = 0.5
            strike_rate_factor = 0.5

        # Normalize run difference (50+ runs per game difference is significant)
        run_diff_factor = min(max(run_difference / 100.0, -0.5), 0.5) + 0.5

        # Combine all factors with weights
        strength = (
            (win_rate * 0.35)  # Win rate is most important
            + (batting_strength * 0.25)  # Batting quality
            + (bowling_strength * 0.25)  # Bowling quality
            + (run_diff_factor * 0.10)  # Run differential
            + (strike_rate_factor * 0.05)  # Aggression/strike rate
        )

        final_strength = min(max(strength, 0), 1)  # Clamp between 0 and 1
        print(f"✅ Team {team_id} strength calculated")
        return final_strength
