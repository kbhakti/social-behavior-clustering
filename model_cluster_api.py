from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model and preprocessor
model = joblib.load('kmeans_model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/predict-cluster', methods=['POST'])
def predict_cluster():
    data = request.get_json()
    df = pd.DataFrame([data])
    X = preprocessor.transform(df)
    cluster = model.predict(X)[0]
    return jsonify({'cluster': int(cluster)})

if __name__ == '__main__':
    app.run(debug=True)