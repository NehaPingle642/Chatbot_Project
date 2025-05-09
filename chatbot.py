"""
import json
import pickle
import os

def load_model():
    try:
        model_path = os.path.join("models", "chatbot_model.pkl")
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except (pickle.UnpicklingError, FileNotFoundError, EOFError) as e:
        print(f"Error loading model: {str(e)}")
        return None

def load_faq_data():
    try:
        faq_path = os.path.join("data", "faq.json")
        with open(faq_path, "r") as f:
            data = json.load(f)
            return data["faq"] if "faq" in data else None
    except FileNotFoundError as e:
        print(f"Error loading FAQ data: {str(e)}")
        return None

# Load the trained ML model
model = load_model()
if model is None:
    print("Failed to load model. Please ensure the model file exists and is valid.")
    exit(1)

print("Model loaded successfully!")

# Load the questions and answers from JSON file
faq_data = load_faq_data()
if faq_data is None:
    print("Failed to load FAQ data. Please ensure the data file exists.")
    exit(1)

# Extract questions and answers from the loaded data
questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

#Predict the answer using the trained model
def get_ml_response(user_input):
    try:
        # Load data if not already loaded
        faq_data = load_faq_data()
        if not faq_data:
            return "Sorry, I'm having trouble accessing my knowledge base."

        # Simple matching for now
        user_input = user_input.lower()
        for item in faq_data:
            if user_input in item["question"].lower():
                return item["answer"]
        
        return "I'm not sure about that. Could you rephrase your question?"
    except Exception as e:
        print(f"Error in ML response: {str(e)}")
        return "Sorry, I encountered an error processing your request."

#  Test output
if __name__ == "__main__":
    print("Chatbot ML Response Mode 🔮")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Bye bye Chill Buddy! See you soon!")
            break
        print("Chatbot:", get_ml_response(user_input))
        """

import json
import pickle
import os
import logging

# Setup logging for better traceability
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_model():
    try:
        model_path = os.path.join("models", "chatbot_model.pkl")
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except (pickle.UnpicklingError, FileNotFoundError, EOFError) as e:
        logging.error(f"Error loading model: {str(e)}")
        return None

def load_faq_data():
    try:
        faq_path = os.path.join("data", "faq.json")
        with open(faq_path, "r") as f:
            data = json.load(f)
            return data["faq"] if "faq" in data else None
    except FileNotFoundError as e:
        logging.error(f"Error loading FAQ data: {str(e)}")
        return None

# Load the trained ML model
model = load_model()
if model is None:
    logging.error("Failed to load model. Please ensure the model file exists and is valid.")
    exit(1)

logging.info("Model loaded successfully!")

# Load the questions and answers from JSON file
faq_data = load_faq_data()
if faq_data is None:
    logging.error("Failed to load FAQ data. Please ensure the data file exists.")
    exit(1)

# Extract questions and answers from the loaded data
questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

# Global FAQ data caching
def get_ml_response(user_input):
    try:
        if not faq_data:
            return "Sorry, I'm having trouble accessing my knowledge base."

        user_input = user_input.lower()
        for item in faq_data:
            if user_input in item["question"].lower():  # Exact match can be improved
                return item["answer"]
        
        return "I'm not sure about that. Could you rephrase your question?"
    except Exception as e:
        logging.error(f"Error in ML response: {str(e)}")
        return "Sorry, I encountered an error processing your request."

# Test output
if __name__ == "__main__":
    logging.info("Chatbot ML Response Mode 🔮")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            logging.info("Chatbot: Bye bye Chill Buddy! See you soon!")
            break
        print("Chatbot:", get_ml_response(user_input))
