import asyncio
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

server_params=StdioServerParameters(
    command="venv/bin/python",
    args=["mcp_server.py"],
    env=None
)

async def main():

    async with stdio_client(server_params) as (read_stream,write_stream):
        async with ClientSession(read_stream,write_stream) as session:
            await session.initialize()
            tools_response=await session.list_tools()
            print("Available tools:",[t.name for t in tools_response.tools])

if __name__=="__main__":
    asyncio.run(main())