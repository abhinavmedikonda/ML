# from flask import Flask, request, jsonify
# import joblib

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return '''
#         <html>
#             <body>
#                 <h1>Decision Tree Model</h1>
#                 <form action="/predict" method="post">
#                     <label for="website_visits">Website Visits:</label>
#                     <input type="number" id="website_visits" name="website_visits"><br><br>
#                     <label for="time_spent_on_website">Time Spent on Website:</label>
#                     <input type="number" id="time_spent_on_website" name="time_spent_on_website"><br><br>
#                     <input type="submit" value="Predict">
#                 </form>
#             </body>
#         </html>
#     '''

# @app.route('/predict', methods=['POST'])
# def predict():
#     website_visits = request.form['website_visits']
#     time_spent_on_website = request.form['time_spent_on_website']

#     # Create a new input data frame
#     new_data = pd.DataFrame({'website_visits': [website_visits], 'time_spent_on_website': [time_spent_on_website]})

#     clf = joblib.load('model.pkl')
#     # Make predictions using the trained model
#     prediction = clf.predict(new_data)

#     return '''
#         <html>
#             <body>
#                 <h1>Prediction Result:</h1>
#                 <p>Expected Status: {}</p>
#             </body>
#         </html>
#     '''.format(prediction[0])

# if __name__ == '__main__':
#     app.run(debug=True)




import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main, view=ft.AppView.WEB_BROWSER)