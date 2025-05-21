# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Castaway is an MCP (Model Capabilities Provider) server designed to interact with Ethereum blockchain applications. It serves as a bridge allowing MCP clients like Claude Desktop, Claude Code, and Raycast to make smart contract calls, send transactions, and retrieve chain data from Ethereum and other EVM-compatible blockchains.

## Environment Setup

- The project uses Python 3.13+ and relies on `uv` for package management
- Set up the environment variables by copying `.env.example` to `.env` and configuring your RPC URL

## Development Commands

```bash
# Activate the virtual environment
source ./.venv/bin/activate

# Run Castaway in local development mode
uv run --with fastmcp fastmcp run castaway.py:mcp

# Install dependencies (if needed)
uv pip install -e .
```

## Project Architecture

The project follows a simple structure:

- `castaway.py`: Main application file that defines the MCP server and blockchain interaction tools
- The application uses FastMCP to expose blockchain interaction capabilities as tools
- Each blockchain interaction is implemented as a tool method that can be called by MCP clients

## Key Components

1. **FastMCP Server**: The core server that exposes blockchain capabilities to MCP clients
2. **Web3 Integration**: Uses web3.py to interact with Ethereum nodes via RPC
3. **Environment Configuration**: Uses dotenv to load configuration like RPC endpoints

## Adding New Blockchain Functionality

When adding new blockchain functionality:

1. Add new tool methods to the `castaway.py` file using the `@mcp.tool()` decorator
2. Each tool should handle one specific blockchain interaction
3. Update the server instructions to document the new capabilities
4. Consider adding any required environment variables to `.env.example`

## Integration with Claude Desktop

For Claude Desktop usage, the configuration needs to be added to `claude_desktop_config.json` as described in the README.md.