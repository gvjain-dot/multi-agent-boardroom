from utils.agent_base import Agent

class CEOAgent(Agent):
    """CEO Agent: defines vision and high-level strategy."""

    def contribute(self, topic: str) -> str:
        return (
            f"As the CEO, my vision for '{topic}' is to define the big picture, "
            "set direction, and align long-term strategy."
        )
