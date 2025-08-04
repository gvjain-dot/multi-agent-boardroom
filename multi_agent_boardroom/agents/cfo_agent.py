from utils.agent_base import Agent

class CFOAgent(Agent):
    """CFO Agent: evaluates financial risks and viability."""

    def contribute(self, topic: str) -> str:
        return (
            f"As the CFO, I will analyze '{topic}' from a financial perspective, "
            "estimating costs, funding needs, and potential ROI."
        )
