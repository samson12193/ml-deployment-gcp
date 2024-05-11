from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load pre-trained model
HR_Recruitment = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = HR_Recruitment.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'Employee Starting Salary Forecast: $ {output}')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = HR_Recruitment.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

# Required for Google Cloud Functions
def predict_http(request):
    with app.test_request_context():
        return app.full_dispatch_request()

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug=True)