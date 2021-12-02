from flask_login import current_user, login_required, login_user, logout_user
from app import app, db
import datetime

from flask import (abort, flash, redirect, render_template, request,
                   send_from_directory, url_for)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

# @app.route('/index')
# def register():
#     """Register a new user"""
#     pass

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:  
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data.lower()).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     return render_template('login.html', title='Sign In', form=form)


# @app.route('/create_speech/', methods=['GET', 'POST'])
# @login_required
# def create_speech():
#     """Create speech"""
#     pass


# @app.route('/view_schedule')
# @login_required
# def view_schedule():
#     return render_template('view_schedule.html', title='View Schedule')


# @app.route('/signup')
# def signup_role():
#     """Sign up to a role"""
#     return render_template('signup.html', title='Signup')
