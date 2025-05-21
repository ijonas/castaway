# Castaway

Castaway is an MCP server that is a Swiss Army knife for interacting with Ethereum applications from MCP clients such as Claude Desktop, Claude Code, and Raycast. You can make smart contract calls, send transactions, or retrieve any type of chain data - all from your MCP client software!

## Installation

We recommend creating an `mcp` folder inside your home directory to collect and assemble all your local MCPs.

    mkdir ~/mcp 
    cd ~/mcp
    git clone https://github.com/ijonas/castaway.git
    cd castaway
    uv venv
    source ./.venv/bin/activate
    uv pip install -e

## Claude Desktop Installation

We recommend creating an `mcp` folder inside your home directory to collect and assemble all your local MCPs.

Add the following fragment to you Claude Desktop `claude_desktop_config.json`:

    "castaway": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/home/user/mcp/castaway",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "castaway.py:mcp"
      ],
      "env": {
        "RPC_URL": "https://sepolia.drpc.org"
      }
    }
    
## Development

To run Castaway in local development mode:

    uv run --with fastmcp fastmcp run castaway.py:mcp
