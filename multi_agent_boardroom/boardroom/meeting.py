from agents.ceo_agent import CEOAgent
from agents.cto_agent import CTOAgent
from agents.cfo_agent import CFOAgent

class BoardRoom:
    def __init__(self, topic: str):
        self.topic = topic
        self.agents = [
            CEOAgent("CEO"),
            CTOAgent("CTO"),
            CFOAgent("CFO"),
        ]
        self.discussion = []  # keep track of conversation

    def run_meeting(self):
        # For console debugging
        print(f"=== Boardroom Discussion on: {self.topic} ===\n")

        for agent in self.agents:
            # Build context from what has been said so far
            context = "\n".join(
                [f"{a}: {m}" for a, m in self.discussion]
            )
            prompt = (
                f"Topic: {self.topic}\n"
                f"Previous discussion:\n{context}\n\n"
                f"Now, {agent.name}, contribute your thoughts."
            )

            response = agent.contribute(prompt)

            # Store
            self.discussion.append((agent.name, response))

            # Still print for console (optional)
            print(f"{agent.name}: {response}\n")

        print("=== End of Meeting ===")

        # ✅ Return discussion so UI can use it
        return self.discussion
