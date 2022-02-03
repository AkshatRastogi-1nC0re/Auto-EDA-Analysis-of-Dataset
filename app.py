import time

from flask import Flask, render_template, request, jsonify
import pandas as pd
import pandas_profiling
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/eda', methods=['POST'])  # This will be called from UI
def eda_operation():
    if request.method == 'POST':

        csv_path = request.form['path_to_csv']
        df = pd.read_csv(csv_path)
        filename = os.path.basename(csv_path).split(".")[0]
        profile = pandas_profiling.ProfileReport(df, minimal=True)
        profile.to_file("templates/{}.html".format(filename))
        return render_template("{}.html".format(filename))


if __name__ == '__main__':
    app.run()
