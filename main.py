import sys
import asyncio

from src.agent import analyze_match


async def main():
    if len(sys.argv) != 3:
        print("Usage: python cli.py <team_a_id> <team_b_id>")
        print("Example: python cli.py 1 2")
        return

    try:
        team_a_id = int(sys.argv[1])
        team_b_id = int(sys.argv[2])

        print(f"🏆 Analyzing match between Team {team_a_id} vs Team {team_b_id}...")
        print("=" * 50)

        analysis = await analyze_match(team_a_id, team_b_id)
        print("✨ Analysis complete!")
        print("=" * 50)
        print(f"🎯 Predicted Winner: {analysis.winner}")
        print(f"📊 Win Probability: {analysis.win_probability:.1%}")
        print(f"🏠 Home Team Strength: {analysis.home_team_strength:.2f}")
        print(f"✈️  Away Team Strength: {analysis.away_team_strength:.2f}")
        print("\n💭 Reasoning:")
        print(analysis.reasoning)
        print("\n🔑 Key Factors:")
        for factor in analysis.key_factors:
            print(f"  • {factor}")

    except ValueError:
        print("Error: Team IDs must be integers")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
