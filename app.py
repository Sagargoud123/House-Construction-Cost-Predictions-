import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Extract input features
        features = np.array([
            data["Area"],
            data["LaborCost"],
            data["MaterialType"],
            data["Pipes"],
            data["Lights"],
            data["Fans"],
            data["Steel"],
            data["Bricks"]
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]

        return jsonify({"EstimatedCost": round(float(prediction), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
