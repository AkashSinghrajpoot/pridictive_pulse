from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and feature columns
model = pickle.load(open("model.pkl", "rb"))
model_columns = pickle.load(open("model_columns.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form
        input_data = {
            'Gender': request.form['Gender'],
            'Age': request.form['Age'],
            'Patient': request.form['Patient'],
            'Severity': request.form['Severity'],
            'BreathShortness': request.form['BreathShortness'],
            'VisualChanges': request.form['VisualChanges'],
            'NoseBleeding': request.form['NoseBleeding'],
            'Systolic': request.form['Systolic'],
            'Diastolic': request.form['Diastolic'],
            'ControlledDiet': request.form['ControlledDiet']
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # One-hot encode
        input_encoded = pd.get_dummies(input_df)
        input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

        # Predict
        prediction = model.predict(input_encoded)[0]

        # ✅ Render result.html with both user data and prediction
        return render_template('result.html', user_data=input_data, prediction=prediction)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
