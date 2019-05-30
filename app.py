# imports for flask app
import os
from flask import Flask, render_template

# create the app
# change the template folder to adjust to the directory structure being used
app = Flask(__name__, template_folder='./resources/templates/')

# route to the home page
# renders a static web page
@app.route("/")
def home():
    return render_template("index.html")

# route for projects page
# opens up projects.json and dynamically populates page with different projects using jinja
@app.route("/projects")
def projects():

    return render_template("project.html")
