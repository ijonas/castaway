from fastmcp import FastMCP
from web3 import Web3
import os
from dotenv import load_dotenv
from address_book import (
    add_address,
    get_address,
    get_all_addresses,
    update_address,
    delete_address,
)

load_dotenv()
RPC_URL = os.getenv("RPC_URL")

mcp = FastMCP(
    name="castaway",
    instructions="""
        This server provides a multitude of tools to allow you to interact with EVM blockchains.
        
        Ethereum Tools:
        - eth_balance(address) - Retrieve the ETH balance of an address
        
        Address Book Tools:
        - address_add(name, evm_address) - Add a name-to-address mapping
        - address_get(name) - Get the Ethereum address for a given name
        - address_list() - List all name-to-address mappings
        - address_update(name, evm_address) - Update the address for a name
        - address_delete(name) - Delete a name-to-address mapping
        """,
)


@mcp.tool()
def eth_balance(address: str) -> str:
    """Retrieve the ETH balance of an address."""
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    # Try to resolve name if not an Ethereum address
    if not address.startswith("0x"):
        resolved_address = get_address(address)
        if not resolved_address.startswith("No address"):
            address = resolved_address
    
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, "ether")
    return f"{balance_eth}"


@mcp.tool()
def address_add(name: str, evm_address: str) -> str:
    """Add a new name-to-address mapping to the address book."""
    return add_address(name, evm_address)


@mcp.tool()
def address_get(name: str) -> str:
    """Get the Ethereum address for a given name."""
    return get_address(name)


@mcp.tool()
def address_list() -> dict:
    """List all name-to-address mappings in the address book."""
    return get_all_addresses()


@mcp.tool()
def address_update(name: str, evm_address: str) -> str:
    """Update the address for a name in the address book."""
    return update_address(name, evm_address)


@mcp.tool()
def address_delete(name: str) -> str:
    """Delete a name-to-address mapping from the address book."""
    return delete_address(name)


if __name__ == "__main__":  # Fixed typo from "main" to "__main__"
    mcp.run()
