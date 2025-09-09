from utils.agent_base import Agent
from utils.config import groq_client 
class CFOAgent(Agent):
    """CFO Agent: powered by LLM for financial viability."""

    # def contribute(self, topic: str) -> str:
    #     prompt = f"You are a CFO. Evaluate the financial risks, costs, and ROI for: {topic}"
    #     response = client.chat.completions.create(
    #         model="gpt-5-mini",
    #         messages=[{"role": "user", "content": prompt}]
    #     )
    #     return response.choices[0].message.content.strip()
    def contribute(self, topic: str) -> str:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": f"You are a CFO. Evaluate the financial risks, costs, and ROI for: {topic}"}]
        )
        return response.choices[0].message.content