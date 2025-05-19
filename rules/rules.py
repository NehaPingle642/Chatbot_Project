# rules/rules.py

def rule_based_response(user_input):
    rules = {
        "hi": "Hello there! How can I help you today?",
        "hello": "Hey! Need any help?",
        "bye": "Goodbye! Have a great day!",
        "thanks": "You're welcome!",
        "who are you": "I'm your friendly chatbot here to assist you"
    }

    # Convert user input to lowercase to avoid case mismatch
    user_input = user_input.lower()
   
    # Check if any rule keyword exists in the input
    for key in rules:
        if key in user_input:
            return rules[key]
        
    # Move this OUTSIDE the loop
    return None
