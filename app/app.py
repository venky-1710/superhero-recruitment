# app.py

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from flask import Flask, render_template, request, redirect, url_for

# Load and preprocess data
df = pd.read_csv('./static/your_newherodata.csv')
ability_dict = {
    "flying": 0, "superhuman strength": 1, "will power": 2, "Superhuman Reflexes": 3,
    "Teleportation": 4, "Super Speed": 5, "Shape shifing": 6, "Time Travel": 7,
    "Elasticity": 8, "Heat Vision": 9
}
df['ability_value'] = df['abilities'].map(ability_dict)

# Feature engineering
df['efficiency'] = df['sucessrate'] * df['missionscompleted'] / 100

# Prepare features and target
X = df[['ability_value', 'strengths', 'weaknesses', 'efficiency']]
y = df['Mission']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"Train accuracy: {train_accuracy:.2f}")
print(f"Test accuracy: {test_accuracy:.2f}")

# Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        ability = request.form['abilities']
        strength = int(request.form['strengths'])
        weakness = 1 if request.form['weaknesses'] == 'Yes' else 0
        success_rate = float(request.form['successrate'])
        missions = int(request.form['missioncompleted'])
        
        ability_value = ability_dict.get(ability, -1)
        efficiency = success_rate * missions / 100
        
        features = np.array([[ability_value, strength, weakness, efficiency]])
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1]
        
        return render_template('predict.html', prediction=prediction, probability=probability)
    else:
        # If it's a GET request, redirect to the home page
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=2202)