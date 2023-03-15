from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
from utils.map import func
import requests
import config
import pickle
import io
# from utils.model import ResNet9


app = Flask(__name__)

@ app.route('/')
def home():
    map = func()
    return render_template('index.html',map=map._repr_html_())


if __name__ == "__main__":
    app.run(debug=False)