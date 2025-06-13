# MCP Visualizer Demo

A complete **Model Context Protocol (MCP)** demonstration with a web-based tool catalog and invocation interface.

## 🚀 Quick Start

```bash
./Start-App.sh
```

Visit **http://localhost:8080** to interact with MCP tools through the web interface.

## 📋 What It Does

- **Discover MCP Tools**: `GET /mcp/v1/tools` - Lists available tools
- **Invoke Tools**: `POST /mcp/v1/tools/<name>` - Executes tools and returns JSON
- **Web Interface**: Interactive tool catalog with real-time results

## 🏗️ Architecture

**4 Docker Containers:**
- **Frontend** (Nginx) - Static web interface + proxy
- **Backend** (FastAPI) - REST API server  
- **Database** (PostgreSQL) - Data storage with auto-seeding
- **MCP Server** (Python) - Model Context Protocol implementation

## 🛠️ Features

- ✅ **Single-port exposure** (8080 only)
- ✅ **Zero build steps** (pure HTML + JS)
- ✅ **Auto-seeded database** 
- ✅ **Complete MCP protocol** implementation
- ✅ **< 60s build time**

## 📁 Project Structure

```
├── frontend/           # Static web interface
├── backend/           # FastAPI REST server
├── mcp-server/        # MCP protocol server
├── db/               # Database initialization
├── docker-compose.yml
└── Start-App.sh      # One-command launcher
```

## 🔧 Available Tools

- **`items_table`** - Returns all items from the database

## 🎯 Demo Flow

1. Web page loads and discovers available MCP tools
2. Click any tool button to invoke it
3. JSON response displays in-browser
4. All interactions use standard MCP protocol endpoints

Built following the **MCP Visualizer Blueprint** for rapid deployment and demonstration.