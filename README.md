# AI Agent Framework

A modular Python framework for building AI agents with function calling capabilities, goal-oriented behavior, and memory management.

## Features

-   **Modular Architecture**: Clean separation of concerns with organized package structure
-   **Goal-Oriented Agents**: Define multiple goals with priorities for agent behavior
-   **Function Calling**: Built-in support for LLM function calling with automatic tool registration
-   **Memory Management**: Conversation history and context management
-   **Extensible Tools**: Easy-to-add custom tools and actions
-   **LiteLLM Integration**: Support for multiple LLM providers through LiteLLM

## Installation

### Install from Git (Recommended)

You can install the AIA framework directly from Git:

```bash
# Install latest version from main branch
pip install git+https://github.com/recepdemrci/aia.git
```

### Development Installation

For development, clone the repository and install in editable mode:

```bash
git clone https://github.com/recepdemrci/aia.git
cd aia
pip install -e .
```

### Environment Setup

Set up your LLM API key (OpenAI or other LiteLLM-supported providers):

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Quick Start

After installation, you can use the framework in your projects:

```python
# Import the main components
from aia import Agent, Goal, Environment, ActionRegistry
from aia.language import AgentFunctionLanguage
from aia.llm import Client


# Define goals
goals = [
    Goal(priority=1, name="Analysis", description="Analyze the project files"),
    Goal(priority=2, name="Complete", description="Provide summary and terminate")
]

# Create agent
agent = Agent(
    goals=goals,
    agent_language=AgentFunctionLanguage(),
    action_registry=ActionRegistry(tags=["file_operations", "system"]),
    client=Client(),
    environment=Environment()
)

# Run agent
memory = agent.run("Analyze the Python files in this project")
```

## Architecture

The framework is organized into the following packages:

### Core Components

-   **Agent** (`src/agent.py`): Main agent class that orchestrates the execution loop
-   **Goal** (`src/core/goal.py`): Dataclass for defining agent objectives with priorities
-   **Action** (`src/core/action.py`): Represents executable functions with metadata
-   **Memory** (`src/core/memory.py`): Manages conversation history and context
-   **Environment** (`src/core/environment.py`): Handles action execution and result formatting

### Actions (`src/registry/`)

-   **ActionRegistry**: Manages and filters available actions
-   **decorators**: Tool registration decorators and utilities

### Language (`src/language/`)

-   **AgentLanguage**: Abstract base for agent communication protocols
-   **AgentFunctionLanguage**: Implementation for function calling

### LLM Integration (`src/llm/`)

-   **Prompt**: Dataclass for structuring LLM prompts
-   **Client**: LLM client functions with LiteLLM integration

## Creating Custom Tools

Tools are created using the `@register_tool` decorator:

```python
from aia import register_tool

@register_tool(tags=["custom"], terminal=False)
def my_custom_tool(param1: str, param2: int = 10) -> str:
    """Description of what this tool does.

    Args:
        param1: Description of param1
        param2: Description of param2 (optional, defaults to 10)

    Returns:
        Description of return value
    """
    return f"Processed {param1} with value {param2}"
```

## Configuration

The framework supports various configuration options:

-   **LLM Model**: Configure in `src/llm/client.py` (default: "openai/gpt-4o")
-   **Max Iterations**: Set in agent.run() method (default: 50)
-   **Tool Filtering**: Use tags or tool names in ActionRegistry

## Dependencies

-   `litellm`: For LLM provider integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your changes with appropriate tests
4. Submit a pull request

## License

This project is open source. Please see the license file for details.
