import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def index():
    df = pd.read_csv("../cities.csv")
    return render_template("data.html", df=[df.to_html(classes='data')], titles=df.columns.values)


if __name__ == "__main__":
    app.run(debug=True)