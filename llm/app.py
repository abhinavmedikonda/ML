from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '''
        <html>
            <body>
                <h1>Decision Tree Model</h1>
                <form action="/predict" method="post">
                    <label for="website_visits">Website Visits:</label>
                    <input type="number" id="website_visits" name="website_visits"><br><br>
                    <label for="time_spent_on_website">Time Spent on Website:</label>
                    <input type="number" id="time_spent_on_website" name="time_spent_on_website"><br><br>
                    <input type="submit" value="Predict">
                </form>
            </body>
        </html>
    '''

@app.route('/predict', methods=['POST'])
def predict():
    website_visits = request.form['website_visits']
    time_spent_on_website = request.form['time_spent_on_website']

    # Create a new input data frame
    new_data = pd.DataFrame({'website_visits': [website_visits], 'time_spent_on_website': [time_spent_on_website]})

    clf = joblib.load('model.pkl')
    # Make predictions using the trained model
    prediction = clf.predict(new_data)

    return '''
        <html>
            <body>
                <h1>Prediction Result:</h1>
                <p>Expected Status: {}</p>
            </body>
        </html>
    '''.format(prediction[0])

if __name__ == '__main__':
    app.run(debug=True)