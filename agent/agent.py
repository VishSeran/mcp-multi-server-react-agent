
from config.config import MODEL_NAME
from config.logger import get_logger


logger = get_logger("agent")

class ReactAgent:
    
    def __init__(self, model_name=MODEL_NAME):
        
        
        try:
            
            if not model_name:
                raise ValueError("model name is missing")
            
            
        
        except ValueError as e:
            logger.error(f"Value error: {e}")
            raise
        
        except Exception as e:
            logger.error(f"Error in react agent: {e}")
            raise