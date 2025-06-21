from mcp.server.fastmcp import FastMCP

server = FastMCP('stdio_server')

@server.tool()
def hello(name: str) -> str:
    """return hello world!"""
    return f"Hello, {name}"

if __name__ == "__main__":
    server.run(transport="streamable-http")
