from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


def foo(x):
    return x.split()


model = pickle.load(open("SVC(class_weight='balanced').pkl",'rb'))


# @app.route('/')
# def index():
#     print("index start")
#     return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        sc = request.form['script']
        pred = model.predict([sc])
        return render_template('response.html',data=pred)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)