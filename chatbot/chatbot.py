from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import os

class Chatbot:
    def __init__(self):
        # Initialize TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer()
        # Load FAQ data from JSON file
        self.faq_data = self.load_faq()
        # Prepare question-answer pairs
        self.questions = [qa['question'] for qa in self.faq_data]
        self.answers = [qa['answer'] for qa in self.faq_data]
        # Create TF-IDF matrix for questions
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def load_faq(self):
        # Get path to FAQ JSON file
        faq_path = os.path.join(os.path.dirname(__file__), 'data', 'faq.json')
        # Load and parse JSON data
        with open(faq_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        return data['faq']

    def get_response(self, user_input):
        # Vectorize user input
        input_vector = self.vectorizer.transform([user_input])
        # Calculate similarity scores
        similarities = cosine_similarity(input_vector, self.question_vectors)
        # Find most similar question
        best_match = similarities.argmax()
        # Return corresponding answer
        return self.answers[best_match]

# Create a global instance
chatbot = Chatbot()

# Export the get_response function
def get_response(user_input):
    return chatbot.get_response(user_input)
