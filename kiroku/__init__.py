from flask import Flask

app = Flask(__name__)
app.config.from_object('kiroku.config')

from kiroku.views import view