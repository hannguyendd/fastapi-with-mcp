# FastAPI with Model Context Protocol (MCP)

A FastAPI application integrated with Model Context Protocol (MCP) for mathematical operations and tool registration examples. This project demonstrates how to build MCP servers using FastAPI and shows different approaches to registering tools.

## Features

- FastAPI web framework integration with MCP
- Multiple mathematical operations (add, multiply, subtract)
- Different tool registration patterns (decorators vs functions)
- Server-Sent Events (SSE) support for real-time communication
- Example configurations for MCP client integration
- Pandas integration for data manipulation demonstrations

## Project Structure

```
fastapi-with-mcp/
├── fastapi_mcp.py          # Main FastAPI + MCP application
├── test_tool_registration.py # Tool registration testing examples
├── config.json             # MCP client configuration
├── pyproject.toml          # Python project configuration
├── .python-version         # Python version specification
├── .gitignore              # Git ignore rules
├── uv.lock                 # UV lock file for dependencies
└── README.md               # This file
```

## Requirements

- Python 3.12+
- FastAPI[standard]
- FastMCP
- Pandas
- Pydantic
- MCP

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd fastapi-with-mcp
```

2. Create a virtual environment (using uv or standard Python):

```bash
# Using uv (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Or using standard Python
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
# Using uv
uv pip install -e .

# Or using pip
pip install -e .
```

## Usage

### Running the FastAPI + MCP Server

Start the main application:

```bash
uvicorn fastapi_mcp:app --reload --port 8000
```

The server will be available at:

- FastAPI docs: `http://localhost:8000/docs`
- MCP SSE endpoint: `http://localhost:8000/mcp-server/sse`
- MCP server mount: `http://localhost:8000/mcp-server`

### Available Tools

The application provides several mathematical tools that demonstrate Pandas integration:

1. **Add** - Add two numbers using pandas DataFrame operations
2. **Multiply** - Multiply two numbers using pandas DataFrame operations
3. **Subtract** - Subtract two numbers using pandas DataFrame operations

Each operation creates a pandas DataFrame to perform the calculation, demonstrating how to integrate data manipulation libraries with MCP tools.

### Tool Registration Methods

This project demonstrates multiple ways to register MCP tools:

#### Method 1: Decorator Approach

```python
@mcp.tool
@app.get("/add", operation_id="add_two_numbers")
async def add(a: int, b: int):
    """Add two numbers and return the sum."""
    summ = pd.DataFrame({"a": [a], "b": [b], "sum": [a + b]})
    result = int(summ.loc[0, "sum"])
    return {"sum": result}
```

#### Method 2: Function Registration

```python
def multiply(a: int, b: int):
    """Multiply two numbers and return the product."""
    product = pd.DataFrame({"a": [a], "b": [b], "product": [a * b]})
    result = int(product.loc[0, "product"])
    return {"product": result}

# Register the function as a tool
mcp.tool(multiply)
```

#### Method 3: Decorator as Function

```python
def subtract(a: int, b: int):
    """Subtract two numbers and return the difference."""
    diff = pd.DataFrame({"a": [a], "b": [b], "difference": [a - b]})
    result = int(diff.loc[0, "difference"])
    return {"difference": result}

# Register using the decorator syntax as a function
mcp.tool()(subtract)
```

#### Method 4: Combined FastAPI + MCP

```python
@app.get("/multiply", operation_id="multiply_two_numbers")
async def multiply_endpoint(a: int, b: int):
    """FastAPI endpoint that also works as MCP tool."""
    return multiply(a, b)

# Register the same function as an MCP tool
mcp.tool(multiply_endpoint)
```

## MCP Client Configuration

The `config.json` file contains example configuration for MCP clients:

```json
{
  "mcpServers": {
    "math-tools": {
      "type": "http",
      "url": "http://localhost:8000/mcp-server/sse",
      "env": {}
    }
  }
}
```

This configuration:

- Uses `"math-tools"` as the server identifier (reflecting the mathematical operations provided)
- Sets type to `"http"` for HTTP-based communication
- Points to the mounted MCP server endpoint at `"/mcp-server/sse"`

## API Endpoints

### FastAPI Endpoints

- `GET /add?a={int}&b={int}` - Add two numbers
- `GET /multiply?a={int}&b={int}` - Multiply two numbers
- `GET /docs` - Interactive API documentation
- `GET /redoc` - ReDoc API documentation

### MCP Endpoints

- `GET /mcp-server/sse` - Server-Sent Events endpoint for MCP communication
- MCP tools are accessible through the MCP protocol via the mounted server at `/mcp-server`

## Development

### Testing Tool Registration

Run the tool registration test to see different registration methods:

```bash
python test_tool_registration.py
```

### Simple MCP Server Example

For testing tool registration methods, see `test_tool_registration.py`:

```bash
python test_tool_registration.py
```

## Dependencies

- **FastAPI[standard]**: Modern, fast web framework for building APIs with standard extras
- **FastMCP**: FastAPI integration for Model Context Protocol
- **Pandas**: Data manipulation library (used for mathematical operations)
- **Pydantic**: Data validation library
- **MCP**: Model Context Protocol implementation

## Environment Variables

This project uses `dotenv` to load environment variables. Create a `.env` file for environment-specific configurations:

```env
# Add any environment variables here if needed
# Example:
# DEBUG=true
# LOG_LEVEL=info
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Learn More

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

## Troubleshooting

### Common Issues

1. **Module name conflicts**: Avoid naming files `mcp.py` as it conflicts with the MCP package
2. **Port conflicts**: Ensure port 8000 is available or change the port in uvicorn command
3. **Python version**: This project requires Python 3.12+
4. **Dependencies**: Make sure all dependencies are installed with the correct versions

### Getting Help

If you encounter issues:

1. Check the FastAPI docs at `/docs` endpoint
2. Verify all dependencies are installed correctly
3. Ensure Python 3.12+ is being used
4. Check server logs for detailed error messages
5. Verify that the MCP SSE endpoint is accessible at `/mcp-server/sse`
