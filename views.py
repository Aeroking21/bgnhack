from flask import Blueprint, render_template
# Blueprint indicates that this file consists of a collection of routes

# Defining the Blueprint
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("index.html")