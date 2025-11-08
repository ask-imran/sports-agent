import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai_litellm import LiteLLMModel
from models import MatchAnalysis
from agent_tools import DataService, register_tools

load_dotenv()

model_name = os.getenv("MODEL_NAME")
api_base = os.getenv("API_BASE_URL")

# Initialize the LiteLLM model
model = LiteLLMModel(
    model_name=model_name,
    api_base=api_base,
)


# Load system prompt from file
def load_system_prompt():
    prompt_file = Path(__file__).parent.parent / "system_prompt.md"
    return prompt_file.read_text(encoding="utf-8")


# Create the agent
sports_agent = Agent(
    model,
    output_type=MatchAnalysis,
    deps_type=DataService,
    system_prompt=load_system_prompt(),
)

# Register tools with the agent
register_tools(sports_agent)


async def analyze_match(team_a_id: int, team_b_id: int) -> MatchAnalysis:
    """Analyze a match between two teams and predict the outcome."""
    data_service = DataService()

    result = await sports_agent.run(
        f"Analyze the upcoming match between team {team_a_id} and team {team_b_id}. "
        f"Get their statistics, calculate their strengths, and predict who will win with probability.",
        deps=data_service,
    )
    return result.output
