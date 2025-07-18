from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('model/rf_model.pkl')
scaler = joblib.load('model/scaler.pkl')
columns = joblib.load('model/columns.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_df = pd.DataFrame([data])
        input_df = pd.get_dummies(input_df)

        for col in columns:
            if col not in input_df.columns:
                input_df[col] = 0
        input_df = input_df[columns]
        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]
        return jsonify({'Predicted_Price': round(prediction, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
