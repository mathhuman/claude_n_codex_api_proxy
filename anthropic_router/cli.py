"""
CLI entry point for anthropic-router.

Provides command-line interface to start the proxy server.
"""

import argparse
import sys
from pathlib import Path

# Add parent directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from start_proxy import main as start_main


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Anthropic Router - HTTP proxy for routing API calls to local CLI tools"
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind the proxy server (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port to bind the proxy server (default: 8080)"
    )
    parser.add_argument(
        "--setup",
        action="store_true",
        help="Run setup/initialization before starting"
    )

    args = parser.parse_args()

    if args.setup:
        from setup_proxy import main as setup_main
        setup_main()

    # Start the proxy server
    start_main()


if __name__ == "__main__":
    main()
