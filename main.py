from fastmcp import FastMCP
from googlesearch import search
import os # Import the os module

mcp = FastMCP("My MCP Server")

@mcp.tool()
def greet(query: str) -> str:
    """Search Any Thing you will get url"""
    # It's good practice to handle potential errors from the search
    try:
        results = [str(url) for url in search(f"{query}", safe="off", lang="en", num_results=10)] # Cast to string if not already
        return "\n".join(results) # Return as a string, perhaps newline separated
    except Exception as e:
        print(f"Error during search: {e}")
        return f"An error occurred: {e}"


if __name__ == "__main__":
    # Get the port from the environment variable Render sets, default to 4200 if not found (for local testing)
    port = int(os.environ.get("PORT", 4200))
    mcp.run(
        transport="sse",
        host="0.0.0.0", # Important for Render
        port=port,      # Important for Render
        log_level="debug",
        path="/my-custom-sse-path",
    )