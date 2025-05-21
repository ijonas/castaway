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
    uv pip install -e .

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
    
## Example Usage from MCP Clients

Here are some examples of how to use Castaway from Claude Desktop, Claude Code, or any other MCP client.

### Checking ETH Balance

Check the ETH balance of an Ethereum address:

```
I'd like to check the ETH balance of 0x71C7656EC7ab88b098defB751B7401B5f6d8976F
```

### Using the Address Book

The address book allows you to associate human-readable names with Ethereum addresses:

**Add an address:**
```
Can you add Vitalik's address to my address book? 
Name: vitalik
Address: 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045
```

**Get an address by name:**
```
What's the address for vitalik?
```

**Check ETH balance using a name:**
```
What's the ETH balance for vitalik?
```

**List all addresses:**
```
Show me all the addresses in my address book
```

**Update an address:**
```
Please update the address for vitalik to 0x71C7656EC7ab88b098defB751B7401B5f6d8976F
```

**Delete an address:**
```
Please remove vitalik from my address book
```

### Additional Examples

These example prompts can be used with Claude Desktop or any other MCP client that has access to the Castaway MCP server.
