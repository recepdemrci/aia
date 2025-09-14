from abc import ABC, abstractmethod
from typing import List
from ..core import Goal, Action, Memory, Environment
from ..llm import Prompt


class AgentLanguage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def construct_prompt(
        self,
        actions: List[Action],
        environment: Environment,
        goals: List[Goal],
        memory: Memory,
    ) -> Prompt:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def parse_response(self, response: str) -> dict:
        raise NotImplementedError("Subclasses must implement this method")
