import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os
import logging

# Set up detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def initialize_model():
    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
        # Ensure directories exist
        models_dir = os.path.join(BASE_DIR, 'models')
        os.makedirs(models_dir, exist_ok=True)
        
        # Load FAQ data
        faq_path = os.path.join(BASE_DIR, 'chatbot', 'data', 'faq.json')
        logger.info(f"Loading FAQ data from: {faq_path}")
        
        # Use utf-8-sig to handle BOM
        with open(faq_path, 'r', encoding='utf-8-sig') as f:
            faq_data = json.load(f)['faq']
        
        # Prepare training data
        questions = [item['question'] for item in faq_data]
        answers = [item['answer'] for item in faq_data]
        
        logger.info(f"Loaded {len(questions)} question-answer pairs")
        
        # Create and train the model
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(questions)
        y = range(len(questions))
        
        model = MultinomialNB()
        model.fit(X, y)
        
        # Save the model
        model_path = os.path.join(models_dir, 'chatbot_model.pkl')
        with open(model_path, 'wb') as f:
            pickle.dump((model, vectorizer, answers), f)
        
        logger.info(f"Model saved successfully to: {model_path}")

    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        logger.error(f"Please ensure the FAQ file exists at: {faq_path}")
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}", exc_info=True)