import asyncio
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
from mcp import ClientSession

# stdio serverの場合はclientプロセス内での立ち上げが必要なので
# その設定を記載
server_params = StdioServerParameters(
    command = "python",
    args=["stdio_server.py"],
    env=None,
)

async def main():
    async with stdio_client(server_params) as (
        read_stream,
        write_stream
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"tools: {tools}")

            result = await session.call_tool("hello", {"name": "owo"})
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
