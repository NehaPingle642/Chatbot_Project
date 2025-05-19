import logging
from rules.rules import rule_based_response
from chatbot import get_ml_response, load_model, load_faq_data

# Setup logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ChocolateBot:
    def __init__(self):
        try:
            # Attempt to load model and FAQ data
            self.model = load_model()
            self.faq_data = load_faq_data()

            # Raise error if FAQ data is missing
            if self.faq_data is None:
                raise RuntimeError("Failed to initialize chatbot - missing FAQ data")
           # logging.info("Bot initialized successfully")

        except Exception as e:
            logging.error(f"Error initializing bot: {e}")
            raise

    def get_response(self, user_input):
        # First try rule-based response
        response = rule_based_response(user_input)
        if response:
           # logging.info(f"Rule-based response: {response}")
           return response

        # If no rule matches, use ML model
        #logging.info("Using ML model for response")
        return get_ml_response(user_input)

def run_chatbot():
    print("Welcome to Chocolate Store Assistant!")
    print("Type 'exit' to end the conversation\n")
    
    try:
        bot = ChocolateBot()
    except RuntimeError as e:
        print(f"Error: {e}")
        return
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'exit':
            print("Thank you for using our chocolate store assistant!")
            #logging.info("User ended the chat session.")
            break

        if user_input == "":
            print("Please enter a valid input.")
            continue

        response = bot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    try:
        run_chatbot()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred. Please try again later.")
