import pickle
import os

def create_pickle_file():
    # FAQ data to be stored
    faq_data = {
        "faq_data": {
            "faq": [
                {
                  "question": "Hii",
                  "answer": "Hello, how can i help you?"
                },
    
                {
                   "question": "Hello",
                   "answer": "Hii, how can i help you?"
                },
                {
                    "question": "Can I customize the chocolate with a name or message?",
                    "answer": "Message-based customization offered"
                },
                {
                    "question": "How many days does delivery take?",
                    "answer": "Fast delivery mentioned, no exact days"
                },
                {
                    "question": "Is same-day delivery available?",
                    "answer": "Important for urgent gifting"
                },
                {
                    "question": "Are your chocolates vegetarian or eggless?",
                    "answer": "Sensitive info for customers"
                },
                {
                    "question": "How do I track my order?",
                    "answer": "Needs integration with courier"
                },
                {
                    "question": "Can I cancel or return a personalized chocolate gift?",
                    "answer": "Policy unclear"
                },
                {
                    "question": "Do you deliver to remote areas or small towns?",
                    "answer": "Pincode checker needed"
                },
                {
                    "question": "Are there any discounts for bulk/corporate gifting?",
                    "answer": "Could use special chatbot flow"
                },
                {
                    "question": "What payment methods are accepted?",
                    "answer": "Needs a quick answer in checkout flow"
                },
                {
                    "question": "What is the shelf life of the chocolates?",
                    "answer": "3 months, made fresh per order"
                },
                {
                    "question": "Which colors can be printed on chocolates?",
                    "answer": "Almost any color, including logos/photos"
                },
                {
                    "question": "Is the printing on the chocolates safe to eat?",
                    "answer": "USFDA-compliant edible colors used"
                },
                {
                    "question": "How can I track my order?",
                    "answer": "Notification via SMS/email"
                },
                {
                    "question": "How do you ensure that the chocolates are not damaged in transit?",
                    "answer": "Packed in sturdy wooden boxes"
                },
                {
                    "question": "What is your return policy?",
                    "answer": "Contact within 24 hrs with photos"
                }
            ]
        }
    }

    # Ensure models directory exists
    models_dir = os.path.join(os.getcwd(), 'models')
    os.makedirs(models_dir, exist_ok=True)

    # Save to pickle file
    pickle_path = os.path.join(models_dir, 'chatbot_model.pkl')
    try:
        with open(pickle_path, 'wb') as file:
            pickle.dump(faq_data, file)
        print(f"Pickle file created successfully at: {pickle_path}")
        return True
    except Exception as e:
        print(f"Error creating pickle file: {str(e)}")
        return False

if __name__ == "__main__":
    create_pickle_file()