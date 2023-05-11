from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


def foo(x):
    return x.split()


model = pickle.load(open("C:\\Users\\Hitesh\\Desktop\\DSBDA-scripts-rating\\SVC(class_weight='balanced').pkl", 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    val1 = request.form['script']

    pred = model.predict([val1])

    return render_template('index.html', data=pred)


if __name__ == '__main__':
    app.run(debug=True)
