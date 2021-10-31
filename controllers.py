from flask import Blueprint, render_template, request, flash
from .models import User
from . import db
import bcrypt
# Blueprint indicates that this file consists of a collection of routes

# Defining the Blueprint
controllers = Blueprint('controllers', __name__)

@controllers.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        repeatPassword = request.form.get('repeatPassword')
        
        # Debugging purposes
        print(email)
        print(password)
        print(repeatPassword)

        # Validation of inputs before adding user to the database
        # Make the errors pop up on screen
        if (not email):
            flash ("Please enter your email")
        elif (not password) or (not repeatPassword):
            flash ("Please enter your password")
        elif (password != repeatPassword):
            flash ("The entered passwords do not match")
        elif (len(email) < 5):
            flash ("Email must be a minimum of 5 characters")
        elif (len(password) < 8):
            flash ("Password must be a minimum of 8 characters")
        else:
            # Add user to database
            hashedPassword = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user = User(email=email, password=hashedPassword)

            # Commit changes to database
            db.session.add(user)
            db.session.commit()
        
    return render_template("register.html")

@controllers.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print(email, password)

        if (len(email) == 0):
            flash ("Please enter your email", category='error')
        elif (len(password) == 0):
            flash ("Please enter your password", category='error')
        else:
            user = User.query.filter_by(email=email).first()
            if (not user):
                flash ("The user is not found", category='error')
            elif (bcrypt.checkpw(password.encode('utf-8'), user.password)):
                flash ("Success", category='success')
                print("Logged in")
                return render_template("index.html")
            else:
                flash ("Password does not match", category='error')

    return render_template("login.html")

@controllers.route('/logout')
def logout():
    return "<p>Logout</p>"