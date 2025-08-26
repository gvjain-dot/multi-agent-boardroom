import os
from openai import OpenAI
from dotenv import load_dotenv
from utils.agent_base import Agent
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CEOAgent(Agent):
    """CEO Agent: powered by LLM for strategy vision."""

    def contribute(self, topic: str) -> str:
        prompt = f"You are a CEO. Provide a startup vision and high-level strategy for: {topic}"
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
