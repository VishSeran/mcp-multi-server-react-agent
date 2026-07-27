

from config.logger import get_logger

logger = get_logger("main")

def main():
    
    try:
        while(True):
            
            choice = input(
                """
                Menu:
                1. Ask the agent a question
                2. Quit
                
                Enter your choice (1 or 2):
                """
            )        
            
            if choice == 1:
                
                print("Enter your question: ")
                query = input("> ")
                
                
    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise
                
    except Exception as e:
        logger.error(f"Error in react agent: {e}")
        raise    