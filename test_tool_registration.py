#!/usr/bin/env python3

from fastmcp import FastMCP

mcp = FastMCP(
    name="Test MCP",
)


# Method 1: Using decorator (current approach)
@mcp.tool
def add_with_decorator(a: int, b: int):
    """Add two numbers using decorator."""
    return {"sum": a + b}


# Method 2: Define function first, then register
def multiply_numbers(a: int, b: int):
    """Multiply two numbers."""
    return {"product": a * b}


# Try to register the function programmatically
try:
    # Let's see what the @mcp.tool decorator actually does
    decorated_multiply = mcp.tool(multiply_numbers)
    print("Method 2a: Using mcp.tool() as a function - SUCCESS")
except Exception as e:
    print(f"Method 2a failed: {e}")

# Method 3: This method doesn't work easily - skip it
print("Method 3: Skipped - requires more complex Tool object creation")


# Method 4: Try different approaches
def divide_numbers(a: int, b: int):
    """Divide two numbers."""
    if b == 0:
        return {"error": "Division by zero"}
    return {"quotient": a / b}


try:
    # Maybe we can call the decorator without @ syntax
    mcp.tool()(divide_numbers)
    print("Method 4: Using mcp.tool()() - SUCCESS")
except Exception as e:
    print(f"Method 4 failed: {e}")

if __name__ == "__main__":
    print("\nAll methods tested!")
