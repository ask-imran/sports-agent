from dotenv import load_dotenv

load_dotenv()
model = OpenAIModel("gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
