from utils.agent_base import Agent
from utils.config import groq_client 

class CEOAgent(Agent):
    def contribute(self, topic: str) -> str:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": f"As the CEO, analyze this idea: {topic}"}]
        )
        return response.choices[0].message.content
