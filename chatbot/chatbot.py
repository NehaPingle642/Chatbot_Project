import json
import pickle
import os
import logging

# Setup logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

def load_model():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(BASE_DIR, 'models', 'chatbot_model.pkl')
        
        with open(model_path, 'rb') as f:
            model, vectorizer, answers = pickle.load(f)
        return model, vectorizer, answers
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        return None, None, None

def load_faq_data():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        faq_path = os.path.join(BASE_DIR, 'chatbot', 'data', 'faq.json')
        
        logger.info(f"Loading FAQ data from: {faq_path}")
        
        with open(faq_path, "r", encoding='utf-8-sig') as f:
            data = json.load(f)
            return data["faq"] if "faq" in data else None
    except FileNotFoundError as e:
        logger.error(f"Error loading FAQ data: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error loading FAQ data: {str(e)}")
        return None

# Load the questions and answers from JSON file
faq_data = load_faq_data()
if faq_data is None:
    logging.error("Failed to load FAQ data. Please ensure the data file exists.")
    exit(1)

# Extract questions and answers from the loaded data
questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

# Global FAQ data caching
def get_response(user_input):
    model, vectorizer, answers = load_model()
    
    if not all([model, vectorizer, answers]):
        return "Sorry, I'm not able to respond right now."
    
    try:
        # Transform user input
        user_vector = vectorizer.transform([user_input])
        
        # Get prediction
        prediction = model.predict(user_vector)[0]
        
        # Return corresponding answer
        return answers[prediction]
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        return "I'm sorry, I couldn't understand that."

# Test output
if __name__ == "__main__":
    logging.info("Chatbot ML Response Mode 🔮")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            logging.info("Chatbot: Bye bye Chill Buddy! See you soon!")
            break
        print("Chatbot:", get_response(user_input))
