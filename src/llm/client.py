import os
import json
from typing import Optional
from litellm import completion
from .prompt import Prompt


class Client:
    def __init__(
        self,
        model: str = "openai/gpt-4o",
        max_tokens: int = 1024,
        api_key: Optional[str] = None,
    ):
        """Initialize Client with required parameters"""
        self.model = model
        self.max_tokens = max_tokens
        self.api_key = api_key

        # Set the API key in environment if provided
        if self.api_key:
            os.environ["OPENAI_API_KEY"] = self.api_key

    def generate_response(self, prompt: Prompt) -> str:
        """Call LLM to get response"""

        messages = prompt.messages
        tools = prompt.tools

        result = None

        if not tools:
            response = completion(
                model=self.model, messages=messages, max_tokens=self.max_tokens
            )
            result = response.choices[0].message.content
        else:
            response = completion(
                model=self.model,
                messages=messages,
                tools=tools,
                max_tokens=self.max_tokens,
            )

            if response.choices[0].message.tool_calls:
                tool = response.choices[0].message.tool_calls[0]
                result = {
                    "tool": tool.function.name,
                    "args": json.loads(tool.function.arguments),
                }
                result = json.dumps(result)
            else:
                result = response.choices[0].message.content

        return result
