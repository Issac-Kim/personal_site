# imports for flask app
import os
from flask import Flask, render_template
app = Flask(__name__)

# route to the home page
# renders a static web page
@app.route("/")
def home():
    return render_template("resources/templates/index.html")

# route for projects page
# opens up projects.json and dynamically populates page with different projects using jinja
@app.route("/projects")
def projects():
    
    return render_template("resources/templates/project.html")
