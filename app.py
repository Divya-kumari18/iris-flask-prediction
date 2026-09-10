from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load trained files
model = joblib.load("model.joblib")
scaler = joblib.load("scaler.joblib")
encoder = joblib.load("encoder.joblib")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    sepal_length = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_length = float(request.form["petal_length"])
    petal_width = float(request.form["petal_width"])

    # User input
    input_data = np.array([[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)

    # Convert encoded value to species name
    species = encoder.inverse_transform(prediction)[0]

    return render_template(
        "index.html",
        prediction=species
    )


if __name__ == "__main__":
    app.run(debug=True)