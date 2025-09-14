"""
AIA Framework - A modular Python framework for building AI agents

This framework provides a comprehensive set of tools for building AI agents with:
- Function calling capabilities
- Goal-oriented behavior
- Memory management
- Extensible tool system
- LLM integration through LiteLLM
"""

from .agent import Agent
from .core import Goal, Action, Memory, Environment
from .registery import ActionRegistry, register_tool
from .language import AgentFunctionLanguage
from .llm import Client

__version__ = "0.1.0"
__author__ = "AIA Framework Contributors"
__email__ = "recepdemiric.14@gmail.com"
__description__ = "A modular Python framework for building AI agents with function calling capabilities, goal-oriented behavior, and memory management"
__url__ = "https://github.com/recepdemrci/aia"

__all__ = [
    "Agent",
    "Goal",
    "Action",
    "Memory",
    "Environment",
    "Client",
    "AgentFunctionLanguage",
    "ActionRegistry",
    "register_tool",
    "__version__",
    "__author__",
    "__description__",
]
