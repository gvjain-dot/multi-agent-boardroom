from agents.ceo_agent import CEOAgent
from agents.cto_agent import CTOAgent
from agents.cfo_agent import CFOAgent

class BoardRoom:
    """Orchestrates a boardroom discussion among multiple agents."""

    def __init__(self, topic: str):
        self.topic = topic
        self.agents = [
            CEOAgent("CEO"),
            CTOAgent("CTO"),
            CFOAgent("CFO")
        ]

    def start_meeting(self):
        print(f"\n=== Boardroom Discussion on '{self.topic}' ===\n")
        for agent in self.agents:
            print(f"{agent.name}: {agent.contribute(self.topic)}")
