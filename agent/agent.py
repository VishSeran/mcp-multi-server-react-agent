import os

import dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver

from config.config import MODEL_NAME
from config.logger import get_logger

dotenv.load_dotenv()
logger = get_logger("agent")

class ReactAgent:
    
    def __init__(self, tools, model_name=MODEL_NAME):
                
        try:
            
            
            GROQ_API = os.getenv("groq_api")
            
            if not GROQ_API:
                raise ValueError("GROQ_API_KEY is missing from environment")
                
            if not model_name:
                raise ValueError("model name is missing")
            
            if not tools:
                raise ValueError("tools list is missing or empty")
     
            self.llm = ChatGroq(
                model=model_name,
                temperature=0.5,
                api_key=GROQ_API
            )
            
            logger.info(f"{model_name} model initiated")
            
            # This allows the agent to remember previous messages in the conversation
            checkpointer = InMemorySaver()
            
            self.react_agent = create_agent(
                model=self.llm,
                tools=tools,
                checkpointer=checkpointer
            )
            
            logger.info("react agent initiated")
         
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
        
        except Exception as e:
            logger.error(f"Error in react agent: {e}")
            raise