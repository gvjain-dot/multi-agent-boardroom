# utils/agent_base.py
from abc import ABC, abstractmethod

class Agent(ABC):
    """Base class for all agents in the boardroom."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def contribute(self, topic: str) -> str:
        """Each agent must implement how they contribute to a given topic."""
        pass
