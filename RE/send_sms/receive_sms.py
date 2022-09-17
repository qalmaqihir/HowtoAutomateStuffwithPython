# Import the flask framework
from flask import Flask


# Creating our flask app
web_app=Flask(__name__)

def flask_url():
    return 'Hello'

web_app.add_url_rule('/','flask_url',flask_url)

web_app.run()

