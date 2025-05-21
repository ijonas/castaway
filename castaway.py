from fastmcp import FastMCP
from web3 import Web3
import os
from dotenv import load_dotenv

load_dotenv()
RPC_URL = os.getenv("RPC_URL")

mcp = FastMCP(
    name="castaway",
    instructions="""
        This server provides a multitude of tools to allow you to interact with EVM blockchains.
        Call eth_balance(address) to retrieve the ETH balance of an address.
        """,
)


@mcp.tool()
def eth_balance(address: str) -> str:
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, "ether")
    return f"{balance_eth}"


if __name__ == "main":
    mcp.run()
