import logging
from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.route("/")
def hello_world():
    app.logger.info("default path (motor) 3")
    return "Hello, World 3!"


@app.route("/hello/<username>")
def hello_user(username):
    # say hello to that user
    app.logger.info("/hello path. User: " + username)
    return "Hello %s" % escape(username)
