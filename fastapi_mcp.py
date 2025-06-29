from fastapi import FastAPI
from fastmcp import FastMCP
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP(
    name="Addition MCP",
)
mcp_app = mcp.streamable_http_app(path="/sse")
app = FastAPI(lifespan=mcp_app.lifespan)


# Method 1: Original decorator approach
@mcp.tool
@app.get("/add", operation_id="add_two_numbers")
async def add(a: int, b: int):
    """Add two numbers and return the sum."""
    summ = pd.DataFrame({"a": [a], "b": [b], "sum": [a + b]})
    result = int(summ.loc[0, "sum"])
    return {"sum": result}


# Method 2: Register function using mcp.tool() as a function call
def multiply(a: int, b: int):
    """Multiply two numbers and return the product."""
    product = pd.DataFrame({"a": [a], "b": [b], "product": [a * b]})
    result = int(product.loc[0, "product"])
    return {"product": result}


# Register the function as a tool
mcp.tool(multiply)


# Method 3: Define function first, then register with mcp.tool()()
def subtract(a: int, b: int):
    """Subtract two numbers and return the difference."""
    diff = pd.DataFrame({"a": [a], "b": [b], "difference": [a - b]})
    result = int(diff.loc[0, "difference"])
    return {"difference": result}


# Register using the decorator syntax as a function
mcp.tool()(subtract)


# Method 4: You can also combine with FastAPI routes
@app.get("/multiply", operation_id="multiply_two_numbers")
async def multiply_endpoint(a: int, b: int):
    """FastAPI endpoint that also works as MCP tool."""
    return multiply(a, b)


# Register the same function as an MCP tool
mcp.tool(multiply_endpoint)


app.mount("/mcp-server", mcp_app)
