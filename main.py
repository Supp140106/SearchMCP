from fastmcp import FastMCP
from googlesearch import search


mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(query: str) -> str:
    """Search Any Thing you will get url"""
    return search(f"{query}",safe=None,region="in",lang="en",num_results=100)
    


if __name__ == "__main__":
    mcp.run()