#!/usr/bin/env python3

import asyncio
import json
import os
import psycopg2
from mcp.server.fastmcp import FastMCP
from mcp.server.session import ServerSession
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import uvicorn
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

# Database configuration
DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "db"),
    "database": os.getenv("POSTGRES_DB", "mydatabase"),
    "user": os.getenv("POSTGRES_USER", "myuser"),
    "password": os.getenv("POSTGRES_PASSWORD", "mypassword")
}

# Create FastMCP server
mcp = FastMCP("MCP Visualizer")

@mcp.tool()
def items_table() -> str:
    """Return id and name for all items from the database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM items")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        result = []
        for row in rows:
            result.append({"id": row[0], "name": row[1]})
        
        return json.dumps({"rows": result})
    except Exception as e:
        return json.dumps({"error": str(e)})

def create_item(name: str) -> str:
    """Create a new item in the database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("INSERT INTO items (name) VALUES (%s) RETURNING id, name", (name,))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        
        return json.dumps({"success": True, "item": {"id": row[0], "name": row[1]}})
    except Exception as e:
        return json.dumps({"error": str(e)})

# HTTP endpoints for the MCP API
async def get_tools(request):
    """Return available tools"""
    tools = [
        {
            "name": "items_table",
            "description": "Return id and name for all items from the database",
            "schema": {
                "type": "object",
                "properties": {},
                "required": []
            }
        },
        {
            "name": "create_item",
            "description": "Create a new item in the database",
            "schema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the item to create"
                    }
                },
                "required": ["name"]
            }
        }
    ]
    return JSONResponse({"tools": tools})

async def invoke_tool(request):
    """Invoke a specific tool"""
    tool_name = request.path_params['name']
    
    if tool_name == "items_table":
        result = items_table()
        return JSONResponse(json.loads(result))
    elif tool_name == "create_item":
        # Get parameters from request body
        try:
            body = await request.json()
            name = body.get("name")
            if not name:
                return JSONResponse({"error": "Missing required parameter: name"}, status_code=400)
            result = create_item(name)
            return JSONResponse(json.loads(result))
        except Exception as e:
            return JSONResponse({"error": f"Invalid request body: {str(e)}"}, status_code=400)
    else:
        return JSONResponse({"error": f"Tool '{tool_name}' not found"}, status_code=404)

# Create Starlette app for HTTP server
app = Starlette(
    routes=[
        Route('/mcp/v1/tools', get_tools, methods=['GET']),
        Route('/mcp/v1/tools/{name}', invoke_tool, methods=['POST']),
    ]
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)