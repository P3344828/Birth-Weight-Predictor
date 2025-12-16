from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = float(form_data['smoke'])

    cleaned_data = {
        'gestation': [gestation],
        'parity': [parity],
        'age': [age],
        'height': [height],
        'weight': [weight],
        'smoke': [smoke]
    }

    return cleaned_data

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

## define your endpoint

@app.route('/predict', methods=['POST'])
def get_prediction():
    # Get data from user
    baby_data_form = request.form

    baby_data_cleaned = get_cleaned_data(baby_data_form)

    ## convert into dataframe
    baby_df = pd.DataFrame(baby_data_cleaned)

    # Load the ML model
    with open('model.pkl', 'rb') as obj:
        model = pickle.load(obj)

    # Make prediction on user data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction), 2)

    # Render result back to HTML
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
