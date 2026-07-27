from config.logger import get_logger
from agent.agent import ReactAgent
from mcp_client.mcp_client_server import MCPServerClient
import asyncio

logger = get_logger("main")

async def main():
    
    try:
        
        mcp_client = MCPServerClient()
        logger.info("Mcp client initialized")
        
        mcp_tools = await mcp_client.get_tools()
        react_agent = ReactAgent(tools=mcp_tools)
        logger.info("React agent initialized")
        
        while(True):
            
            choice = input(
                """
                Menu:
                1. Ask the agent a question
                2. Quit
                
                Enter your choice (1 or 2):
                """
            )
            
            if choice == "1":
                
                print("Enter your question: ")
                query = input("> ")
                
                response = await react_agent.get_response(query)
                print("Response: ", response)
                
            if choice == "2":
                print("Goodbye")
                break
            
            else:
                print("Invalid input, please insert valid input")
                
    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise
                
    except Exception as e:
        logger.error(f"Error in react agent: {e}")
        raise    
    

if __name__ == "__main__":
    
    asyncio.run(main())