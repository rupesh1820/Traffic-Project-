# Hinglish comments for easy samajh 👍

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import os

app = Flask(__name__)
CORS(app)  # frontend ko allow karne ke liye

# 🧠 Sample dataset (demo purpose)
data = pd.DataFrame({
    'time':[18,10,14,20,8,17,9,22],
    'day':[1,0,1,1,0,1,0,1],        # 1 = weekday
    'weather':[2,0,1,2,0,2,0,1],    # 0=sunny,1=cloudy,2=rainy
    'traffic':[2,0,1,2,0,2,0,1]     # 0=low,1=medium,2=high
})

X = data[['time','day','weather']]
y = data['traffic']

# 🤖 Model train
model = RandomForestClassifier()
model.fit(X,y)

# ✅ Home route (test ke liye)
@app.route('/')
def home():
    return "API Running 🚦"

# 🔥 Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        time = int(data['time'])
        day = int(data['day'])
        weather = int(data['weather'])

        result = model.predict([[time, day, weather]])[0]

        labels = ['Low', 'Medium', 'High']

        return jsonify({
            "prediction": labels[result]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


# ✅ Deployment-friendly run (IMPORTANT)
if __name__ == '__main__':
    app.run(
        host='0.0.0.0', 
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )