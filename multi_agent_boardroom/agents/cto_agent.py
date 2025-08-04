from utils.agent_base import Agent

class CTOAgent(Agent):
    """CTO Agent: focuses on technology and implementation."""

    def contribute(self, topic: str) -> str:
        return (
            f"As the CTO, my approach to '{topic}' is to evaluate technical feasibility, "
            "recommend a tech stack, and outline MVP features."
        )
