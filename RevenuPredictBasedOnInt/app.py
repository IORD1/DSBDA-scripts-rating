from flask import Flask, render_template, request
import pickle
import numpy as np
import re
import string



app = Flask(__name__)


def foo(x):
    return x.split()


model = pickle.load(open("randome_f_numeric_revenue",'rb'))


# @app.route('/')
# def index():
#     print("index start")
#     return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        ga1 = request.form['ga1']
        ga2 = request.form['ga2']
        dg = request.form['dg']
        budget = request.form['budget']
        runtime = request.form['runtime']
        print('-----------------------------------------')
        print(ga1,'-',ga2,'-',dg,'-',budget,'-',runtime)
        print('-----------------------------------------')

        pred = model.predict([[ga1,ga2,dg,budget,runtime]])
        pred = np.round(pred,2)
        return render_template('response.html',data=pred)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)