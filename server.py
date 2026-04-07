import os
import pickle
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

# Template path fix
template_dir = os.path.join(os.getcwd(), 'templates')
app = Flask(__name__, template_folder=template_dir)

CORS(app)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'no data'}), 400
    if 'size' not in data:
        return jsonify({'error': 'size missing'}), 400

    try:
        sqft = float(data['size'])
    except:
        return jsonify({'error': 'invalid size'}), 400

    if sqft <= 230:
        return jsonify({'error': 'Size must be greater than 230'}), 400
    if sqft > 1800:
        return jsonify({'error': 'Size exceeds limit of 1800'}), 400

    predicted_price = model.predict([[sqft]])[0]

    return jsonify({
        'price': round(predicted_price, 2),
        'currency': 'USD'
    })

if __name__ == "__main__":
    app.run(debug=True)