from flask import Flask, render_template, request, jsonify
from chat import get_response
import nltk
nltk.download('punkt')

app = Flask(__name__)

@app.route("/")
def index_get():
    return render_template("base.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    text = request.get_json()["message"]
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)
if __name__ == "__main__":
    app.run(debug=True)

