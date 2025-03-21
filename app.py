from flask import Flask, render_template, request
import joblib
import numpy as np

# Load trained model
model = joblib.load("concrete_strength_model.pkl")

# Initialize Flask app
app = Flask(__name__)

# Home route: Displays the input form
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        cement = float(request.form['cement'])
        slag = float(request.form['slag'])
        fly_ash = float(request.form['fly_ash'])
        water = float(request.form['water'])
        superplasticizer = float(request.form['superplasticizer'])
        coarse_agg = float(request.form['coarse_agg'])
        fine_agg = float(request.form['fine_agg'])
        age = int(request.form['age'])

        # Create feature array
        features = np.array([[cement, slag, fly_ash, water, superplasticizer, coarse_agg, fine_agg, age]])

        # Make prediction
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction=f"Predicted Compressive Strength: {prediction:.2f} MPa")

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
