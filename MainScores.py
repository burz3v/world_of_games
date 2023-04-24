from flask import Flask, render_template
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from os.path import exists

app = Flask(__name__)


@app.route("/")
def score_server():
    scores_file = SCORES_FILE_NAME
    if exists(scores_file):
        with open(scores_file, "r", encoding="utf8") as file:
            score = file.readline()
            return render_template("score.html", SCORE = score), 200
    else:
        return render_template("error.html", ERROR = BAD_RETURN_CODE), 404


if __name__ == "__main__":
    app.run(debug=True)