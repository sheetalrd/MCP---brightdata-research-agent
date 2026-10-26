
import asyncio
import os

from dotenv import load_dotenv
from mcp import Client

load_dotenv()

token = os.getenv("BRIGHTDATA_API_TOKEN")

async def main():
    if not token or token == "replace_with_your_actual_token":
        print("ERROR: Check your BRIGHTDATA_API_TOKEN in .env")
        return

    url = f"https://mcp.brightdata.com/mcp?token={token}"

    try:
        async with Client(url) as client:
            result = await client.call_tool(
                "search_engine",
                {"query": "What is Model Context Protocol MCP?"}
            )

            print("\nWeb search completed!\n")
            print(result)

    except Exception as error:
        message = str(error).replace(token, "[REDACTED]")
        print(f"Search failed: {type(error).__name__}")
        print(message)

if __name__ == "__main__":
    asyncio.run(main())
