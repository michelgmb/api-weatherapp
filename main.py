from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

variable = "hello"
@app.route('/')
def home():
    return render_template("home.html", data=variable)


@app.route('/api/v1/<word>/')
def about(word):
    print(word)
    df = pd.read_csv("data/dictionary.csv")
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    print(definition)
    result_dictionary = {'word': word,
                         'Definition': definition}

    return result_dictionary






