"""KubeCon EU MCP Server — Conference guidance via Model Context Protocol."""

from kubecon_eu_mcp.server import mcp


def main() -> None:
    """Entry point for the kubecon-eu-mcp CLI."""
    import sys

    transport = "stdio"
    if "--http" in sys.argv:
        transport = "streamable-http"

    mcp.run(transport=transport)
