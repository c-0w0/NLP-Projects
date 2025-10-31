from pydantic_ai.mcp import MCPServerStdio
from pathlib import Path

project_root = Path.cwd()
data_dir = project_root / "uv" / "data" 

servers = {
    "fetch_server": MCPServerStdio('python', ["-m", "mcp_server_fetch"]),
    "file_server": MCPServerStdio('npx', ["-y", "@modelcontextprotocol/server-filesystem", str(data_dir.resolve())])
}

def get_servers():
    """Return all configured MCP servers as a list.

    Returns:
        list: a list of MCP server instances
    """
    return list(servers.values())