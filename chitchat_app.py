from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory storage for chat messages
messages = []

@app.route('/chat', methods=['POST'])
def send_message():
    content = request.json.get('content')
    if content:
        messages.append(content)
        return jsonify({'message': 'Message received'}), 201
    return jsonify({'error': 'No content provided'}), 400

@app.route('/chat', methods=['GET'])
def get_messages():
    return jsonify({'messages': messages}), 200

if __name__ == '__main__':
    app.run(debug=True)