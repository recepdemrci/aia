from typing import Dict, List, Any

# Global tool registries
tools: Dict[str, Dict[str, Any]] = {}
tools_by_tag: Dict[str, List[str]] = {}


def register(tool_name: str, metadata: Dict[str, Any]) -> None:
    """
    Register tool metadata in the global registry.

    Args:
        tool_name: Name of the tool to register
        metadata: Tool metadata including description, parameters, function, etc.
    """
    tools[tool_name] = {
        "description": metadata["description"],
        "parameters": metadata["parameters"],
        "function": metadata["function"],
        "terminal": metadata["terminal"],
        "tags": metadata["tags"] or [],
    }

    # Update tools_by_tag index
    for tag in metadata.get("tags", []):
        if tag not in tools_by_tag:
            tools_by_tag[tag] = []
        tools_by_tag[tag].append(tool_name)


def get_all() -> Dict[str, Dict[str, Any]]:
    """Get all registered tools."""
    return tools


def get_by_tag(tag: str) -> List[str]:
    """Get all tool names with a specific tag."""
    return tools_by_tag.get(tag, [])


def clear() -> None:
    """Clear all registered tools (useful for testing)."""
    tools.clear()
    tools_by_tag.clear()


def get_count() -> int:
    """Get the total number of registered tools."""
    return len(tools)
