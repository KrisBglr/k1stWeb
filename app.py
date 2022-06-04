from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
loaded_model = joblib.load('dib_75.pkl')

@app.route('/') #decorator
def home():
    return render_template('homepage.html')

@app.route('/predict', methods=['POST'])
def predict():
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))
    print(preg, plas, pres, skin, test, mass, pedi, age)
    prediction = loaded_model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])
    if prediction[0]==1:
        result='Diabetic'
    else:
        result ='Not Diabetic'
    return render_template('result.html', value=result)

#debug=True ensures changes are reflected to page automatically
if __name__ == '__main__':
    app.run(debug=True)