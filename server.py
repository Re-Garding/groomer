"""Server for Grooming Project"""

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from jinja2 import StrictUndefined
import os, model, crud

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")





if __name__ == '__main__':
    model.connect_to_db(app)
    app.run()
    host="0.0.0.0",
    use_reloader=True,
    use_debugger=True,