from utils.agent_base import Agent
from utils.config import groq_client 
class CTOAgent(Agent):
    """CTO Agent: powered by LLM for technical feasibility."""

    # def contribute(self, topic: str) -> str:
    #     prompt = f"You are a CTO. Analyze the technical feasibility and suggest an MVP tech stack for: {topic}"
    #     response = client.chat.completions.create(
    #         model="gpt-5-mini",
    #         messages=[{"role": "user", "content": prompt}]
    #     )
    #     return response.choices[0].message.content.strip()
    def contribute(self, topic: str) -> str:
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": f"You are a CTO. Analyze the technical feasibility and suggest an MVP tech stack for: {topic}"}]
        )
        return response.choices[0].message.content
