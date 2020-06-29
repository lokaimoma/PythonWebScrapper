import functools
from flask import flash, session, redirect, url_for,current_app
from typing import Callable


def requires_login(function: Callable):
    @functools.wraps(function)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash('Log in is required!!!', 'danger')
            return redirect(url_for('users.login'))

        return function(*args, **kwargs)
    return decorated_function


def requires_admin(f: Callable):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        admin = current_app.config.get('ADMIN')
        if session['email'] != admin:
            flash("Admin previlages required!!!!!!!!!!!!!!", "danger")
            return redirect(url_for('users.login'))

        return f(*args, **kwargs)

    return decorated_function

