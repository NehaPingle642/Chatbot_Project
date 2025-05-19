import json
import os

def update_faq_data():
    # Define FAQ entries from existing faq.json
    faq_data = {
        "faq": [
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
            },
            {
                "question": "Can I customize the chocolate with a name or photo?",
                "answer": "Yes, full customization including photos"
            },
            {
                "question": "Do you offer corporate gifting options?",
                "answer": "Yes, includes logos etc."
            },
            {
                "question": "Are there any discounts for bulk orders?",
                "answer": "Info available on request"
            }
        ]
    }

    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname("data/faq.json"), exist_ok=True)

    try:
        # Save to JSON file with proper formatting
        with open("data/faq.json", "w", encoding="utf-8") as f:
            json.dump(faq_data, f, indent=2, ensure_ascii=False)
        print("✅ FAQ data saved successfully!")
    except Exception as e:
        print(f"❌ Error saving FAQ data: {str(e)}")

if __name__ == "__main__":
    update_faq_data()