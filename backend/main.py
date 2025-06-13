from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2, os, httpx, json
from typing import Dict, Any, Optional

cfg = {
    "host": os.getenv("POSTGRES_HOST", "db"),
    "db":   os.getenv("POSTGRES_DB",   "mydatabase"),
    "user": os.getenv("POSTGRES_USER", "myuser"),
    "pw":   os.getenv("POSTGRES_PASSWORD","mypassword")
}

app = FastAPI()

# Pydantic models for AI agent requests
class AIRequest(BaseModel):
    query: str
    context: Optional[str] = None

class MCPToolRequest(BaseModel):
    tool_name: str
    parameters: Optional[Dict[str, Any]] = None

# MCP Server URL
MCP_SERVER_URL = "http://mcp:7000"

@app.get("/api/items")
def items():
    conn = psycopg2.connect(host=cfg["host"], database=cfg["db"],
                             user=cfg["user"], password=cfg["pw"])
    cur  = conn.cursor()
    cur.execute("SELECT id,name FROM items;")
    data = [{"id": r[0], "name": r[1]} for r in cur.fetchall()]
    cur.close(); conn.close()
    return {"items": data}

@app.get("/api/ai/mcp/tools")
async def get_mcp_tools():
    """Get available MCP tools for AI agents"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{MCP_SERVER_URL}/mcp/v1/tools")
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch MCP tools: {str(e)}")

@app.post("/api/ai/mcp/execute")
async def execute_mcp_tool(request: MCPToolRequest):
    """Execute an MCP tool for AI agents"""
    try:
        async with httpx.AsyncClient() as client:
            if request.parameters:
                response = await client.post(
                    f"{MCP_SERVER_URL}/mcp/v1/tools/{request.tool_name}",
                    json=request.parameters,
                    headers={"Content-Type": "application/json"}
                )
            else:
                response = await client.post(f"{MCP_SERVER_URL}/mcp/v1/tools/{request.tool_name}")
            
            if response.status_code == 200:
                return response.json()
            else:
                raise HTTPException(status_code=response.status_code, detail=response.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to execute MCP tool: {str(e)}")

@app.post("/api/ai/agent")
async def ai_agent_interface(request: AIRequest):
    """
    AI Agent interface that can interpret natural language and execute MCP tools
    This simulates how Claude or other AI tools would interact with the MCP server
    """
    try:
        # First, get available tools
        async with httpx.AsyncClient() as client:
            tools_response = await client.get(f"{MCP_SERVER_URL}/mcp/v1/tools")
            tools_data = tools_response.json()
            tools = tools_data.get("tools", [])
        
        # Simple query processing (in a real implementation, this would use an LLM)
        query_lower = request.query.lower()
        results = []
        
        if "list" in query_lower or "show" in query_lower or "get" in query_lower:
            # Execute items_table tool
            async with httpx.AsyncClient() as client:
                response = await client.post(f"{MCP_SERVER_URL}/mcp/v1/tools/items_table")
                if response.status_code == 200:
                    data = response.json()
                    results.append({
                        "action": "list_items",
                        "tool_used": "items_table",
                        "result": data,
                        "interpretation": f"Retrieved {len(data.get('rows', []))} items from the database"
                    })
        
        elif "create" in query_lower or "add" in query_lower or "new" in query_lower:
            # Try to extract item name from query
            # Simple extraction - in real implementation would use NLP
            words = request.query.split()
            item_name = None
            
            # Look for quoted strings or words after "create", "add", "new"
            for i, word in enumerate(words):
                if word.lower() in ["create", "add", "new"] and i + 1 < len(words):
                    # Take the rest of the query as the item name
                    item_name = " ".join(words[i+1:]).strip('"\'')
                    break
            
            if not item_name:
                item_name = "AI Generated Item"
            
            # Execute create_item tool
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{MCP_SERVER_URL}/mcp/v1/tools/create_item",
                    json={"name": item_name},
                    headers={"Content-Type": "application/json"}
                )
                if response.status_code == 200:
                    data = response.json()
                    results.append({
                        "action": "create_item",
                        "tool_used": "create_item",
                        "result": data,
                        "interpretation": f"Created new item: '{item_name}'"
                    })
        
        else:
            # Default: show available tools
            results.append({
                "action": "show_capabilities",
                "available_tools": tools,
                "interpretation": "I can help you list items or create new ones. Try asking 'list items' or 'create a new item called X'"
            })
        
        return {
            "query": request.query,
            "context": request.context,
            "available_tools": [tool["name"] for tool in tools],
            "results": results,
            "usage_examples": [
                "list all items",
                "show me the items", 
                "create a new item called 'My New Item'",
                "add an item named 'Test Item'"
            ]
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI agent error: {str(e)}")

@app.get("/api/ai/status")
async def ai_status():
    """Check AI agent and MCP server connectivity"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{MCP_SERVER_URL}/mcp/v1/tools")
            mcp_status = response.status_code == 200
        
        return {
            "ai_agent": "ready",
            "mcp_server": "connected" if mcp_status else "disconnected",
            "capabilities": [
                "Natural language query processing",
                "MCP tool discovery and execution", 
                "Database operations via MCP protocol"
            ]
        }
    except Exception as e:
        return {
            "ai_agent": "ready",
            "mcp_server": "disconnected",
            "error": str(e)
        }