from flask import Blueprint, render_template, request, url_for, redirect,session
from models import User
from models.users import error 

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            User.register_user(email, password)
            session['email'] = email
            return email
        except error.UserError as e:
            return e.message

    return render_template('users/register.html')

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return email
        except error.UserError as e:
            return e.message

    return render_template('users/login.html')

