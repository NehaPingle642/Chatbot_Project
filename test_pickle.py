import pickle
import os
import json

def test_pickle_file():
    # Use relative path instead of absolute
    file_path = os.path.join('models', 'chatbot_model.pkl')
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            if "faq_data" in data:
                print("✅ Pickle file is valid and contains FAQ data")
                return True
            else:
                print("⚠️ Pickle file is valid but missing FAQ data")
                return False
    except (pickle.UnpicklingError, EOFError) as e:
        print(f"❌ Pickle file is corrupted: {str(e)}")
        return False
    except FileNotFoundError:
        print("❌ Pickle file not found")
        return False

def display_pickle_contents():
    file_path = os.path.join('models', 'chatbot_model.pkl')
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            print("\n📝 Pickle File Contents:")
            print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"❌ Error reading pickle file: {str(e)}")

if __name__ == "__main__":
    if test_pickle_file():
        display_pickle_contents()