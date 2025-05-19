from flask import Flask, render_template, request, jsonify
from chatbot import ChocolateBot

app = Flask(__name__)
bot = ChocolateBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])   # <-- make sure this matches 'fetch' URL
def get_response():
    data = request.get_json()
    user_message = data.get('message')
    bot_reply = bot.get_response(user_message)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)

