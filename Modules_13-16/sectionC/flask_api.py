from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    df = pd.DataFrame([{
        "distance": data["distance"],
        "items": data["items"],
        "weather": data["weather"]
    }])

    prediction = model.predict(df)[0]

    return jsonify({
        "delivery_time": round(float(prediction), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)