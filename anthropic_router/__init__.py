"""
Anthropic Router - HTTP proxy for routing Anthropic/OpenAI API calls to local CLI tools.

This package provides a universal HTTP proxy that automatically routes API calls
to local CLI tools (Claude Code, Codex CLI) based on special API keys.
"""

__version__ = "0.1.0"

# Re-export main components for easier imports
from ..proxy_server import ProxyServer
from ..anthropic_router import AnthropicRouter
from ..openai_router import OpenAIRouter
from ..claude_code_client import ClaudeCodeClient
from ..codex_client import CodexClient

__all__ = [
    "ProxyServer",
    "AnthropicRouter",
    "OpenAIRouter",
    "ClaudeCodeClient",
    "CodexClient",
    "__version__",
]
