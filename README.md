# MCP Multi-Server Agent

A command-line AI agent built with **LangGraph** and **LangChain MCP Adapters** that connects to multiple **Model Context Protocol (MCP)** servers over different transports. The agent can answer questions using up-to-date library documentation (via Context7) and explore The Metropolitan Museum of Art's collection (via the Met Museum MCP server).

## Overview

This project demonstrates how to build a multi-server MCP client and wire it into a ReAct-style LangGraph agent with conversation memory. It's a practical, hands-on example of connecting an LLM to external tools through MCP, using two different transport mechanisms side by side.

## Architecture

```
                    MCP Client
        ┌────────────────────────────────────────┐
        │  Met Museum Session   Context7 Session │
        └───────────┬───────────────┬────────────┘
                STDIO Transport   HTTP Transport
                        │
                        ▼
              LangChain MCP Adapters
                        │
                        ▼
              LangGraph ReAct Agent (GPT-5)
```

- **Context7 MCP server** — connected via **Streamable HTTP** transport, provides access to current library/documentation data from remote repositories. Stateless and cloud-friendly.
- **Met Museum MCP server** — connected via **STDIO** transport, runs as a local Node.js subprocess (`npx metmuseum-mcp`) and exposes tools for querying The Metropolitan Museum of Art's catalogue.
- **LangChain MCP Adapters** convert MCP tools into LangChain-compatible tools.
- **LangGraph `create_react_agent`** builds a ReAct (Reasoning + Acting) agent that decides which tool to call, observes the result, and repeats until it has a final answer.
- **`InMemorySaver`** checkpointing gives the agent short-term conversational memory across turns in a session.

## Features

- Multi-server MCP client supporting both STDIO and Streamable HTTP transports
- ReAct agent powered by `gpt-5-nano` (swappable for other OpenAI models, or IBM watsonx via `ChatWatsonx`)
- Persistent conversation memory within a session using thread-based checkpointing
- Simple looping CLI for interactive Q&A
- Clean, commented code intended as a learning reference for building MCP-powered agents

## Prerequisites

- Python 3.10+
- Node.js and `npx` (required to run the Met Museum MCP server locally)
- An OpenAI API key (or IBM watsonx credentials if using that model instead)
- Basic familiarity with Python and MCP transport concepts

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/mcp-multi-server-agent.git
   cd mcp-multi-server-agent
   ```

2. **Create and activate a virtual environment**
   ```bash
   pip install virtualenv
   virtualenv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install langgraph==0.6.6
   pip install langchain==0.3.27
   pip install langchain-openai==0.3.32
   pip install langchain-ibm==0.3.18
   pip install langchain-mcp-adapters==0.1.9
   ```

4. **Set your API key**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## Usage

Run the application:

```bash
python main.py
```

On startup, the agent introduces itself and its available tools. You'll then see a menu:

```
Menu:
1. Ask the agent a question
2. Quit
Enter your choice (1 or 2):
```

Select **1** to ask a question — try something about a library's documentation (via Context7) or an artwork/artist in The Met's collection (via the Met Museum MCP server). Select **2** to exit.

**Notes:**
- You may see a `Met Museum MCP server running on stdio` message in the terminal when that server is accessed — this is expected and can be ignored.
- The agent retains conversation history for the duration of the running session.
- Responses may take longer as the conversation grows.
- Be mindful of API usage/rate limits when chatting with the agent.

## Project Structure

```
.
├── main.py        # Entry point: MCP client setup, agent creation, CLI loop
└── README.md
```

## Configuration

MCP servers are configured in `main.py` via `MultiServerMCPClient`:

```python
client = MultiServerMCPClient(
    {
        "context7": {
            "url": "https://mcp.context7.com/mcp",
            "transport": "streamable_http",
        },
        "met-museum": {
            "command": "npx",
            "args": ["-y", "metmuseum-mcp"],
            "transport": "stdio",
        },
    }
)
```

Swap in your own MCP servers here to extend the agent with additional tools and data sources.

## Next Steps / Ideas for Extension

- Add more MCP servers (e.g., ones connected to your own data or internal APIs)
- Experiment with different LLMs (larger GPT-5 variants or open-source models)
- Extend the CLI into a web app or chat interface
- Explore more advanced agent patterns: planning, multi-step reasoning, or chaining multiple MCP tools

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

## Authors

- Joshua Zhou — Data Scientist @ IBM
- Joseph Santarcangelo — Data Scientist @ IBM
