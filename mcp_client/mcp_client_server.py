from langchain_mcp_adapters.client import MultiServerMCPClient
from config.logger import get_logger


logger = get_logger("mcp")

class MCPServerClient:
    
    def __init__(self):
        
        try:
            
            self.mcp_client = MultiServerMCPClient(
                {
                    "context7": {
                        "url": "https://mcp.context7.com/mcp",
                        "transport":"streamable_http"
                    },
                    
                    "met-museum": {
                        "command": "npx",
                        "args": ["-y","metmuseum-mcp"],
                        "transport":"stdio"
                    }
                }
            )
            logger.info("mcp client has created")
 
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
                
        except Exception as e:
            logger.error(f"Error in react agent: {e}")
            raise
        
    async def get_tools(self):
        
        try:
            
            tools = await self.mcp_client.get_tools()
            return tools
            
        except ValueError as e:
                    logger.error(f"Value error: {e}")
                    raise
                        
        except Exception as e:
            logger.error(f"Error in get tools: {e}")
            raise