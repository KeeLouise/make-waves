from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User
from app.extensions import db, bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/account')

@auth_bp.route('/', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        if 'login' in request.form:
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully.', 'success')
                return redirect(url_for('auth.account'))
            else:
                flash('Invalid login credentials.', 'danger')

        elif 'register' in request.form:
            username = request.form['username']
            email = request.form['email']
            password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            first_name = request.form['first_name']
            surname = request.form['surname']

            if User.query.filter_by(email=email).first():
                flash('Email already registered.', 'warning')
                return redirect(url_for('auth.account'))

            user = User(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                surname=surname
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Account created and logged in!', 'success')
            return redirect(url_for('auth.account'))

    return render_template('account/account.html', user=current_user if current_user.is_authenticated else None)