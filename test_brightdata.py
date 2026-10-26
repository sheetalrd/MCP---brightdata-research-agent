
import asyncio
import os

from dotenv import load_dotenv
from mcp import Client

load_dotenv()

async def main():
    token = os.getenv("BRIGHTDATA_API_TOKEN")
    if not token:
        print("ERROR: Bright Data token is missing from .env")
        return

    url = f"https://mcp.brightdata.com/mcp?token={token}"

    try:
        async with Client(url) as client:
            result = await client.list_tools()
            print("Connected successfully!")
            for tool in result.tools:
                print("-", tool.name)

    except Exception as error:
        print("Connection failed:", repr(error))
        if isinstance(error, BaseExceptionGroup):
            for item in error.exceptions:
                print("Underlying error:", repr(item))

asyncio.run(main())
