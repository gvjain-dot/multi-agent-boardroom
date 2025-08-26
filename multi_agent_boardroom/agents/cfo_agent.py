import os
from openai import OpenAI
from utils.agent_base import Agent
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class CFOAgent(Agent):
    """CFO Agent: powered by LLM for financial viability."""

    def contribute(self, topic: str) -> str:
        prompt = f"You are a CFO. Evaluate the financial risks, costs, and ROI for: {topic}"
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
