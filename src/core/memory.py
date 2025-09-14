from typing import List, Dict, Optional


class Memory:
    def __init__(self):
        self.items = []  # Basic conversation history

    def add_memory(self, memory: dict):
        """Add memory to working memory"""
        self.items.append(memory)

    def get_memories(self, limit: Optional[int] = None) -> List[Dict]:
        """Get formatted conversation history for prompt"""
        if limit is None:
            return self.items
        return self.items[:limit]

    def copy_without_system_memories(self):
        """Return a copy of the memory without system memories"""
        filtered_items = [m for m in self.items if m["type"] != "system"]
        memory = Memory()
        memory.items = filtered_items
        return memory
