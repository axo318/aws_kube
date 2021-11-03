import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    cwd = os.getcwd()
    ls_out = os.listdir()
    return f"APP ABOUT TO FAIL     CWD: {cwd}, ls output: {ls_out}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')