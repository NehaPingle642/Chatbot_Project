import pickle
import yaml

# Load the pickle file
with open('models/chatbot_model.pkl', 'rb') as f:
    data = pickle.load(f)

# Convert the data to YAML format
with open('chatbot_model.yaml', 'w') as yaml_file:
    yaml.dump(data, yaml_file)

print("Model saved as YAML!")
