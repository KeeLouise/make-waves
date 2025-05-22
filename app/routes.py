from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app.models import User
from app.extensions import db, bcrypt

def register_routes(app):
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template('home/home.html')

    @app.route('/services')
    def services():
        return render_template('services/services.html')

    @app.route('/about')
    def about():
        return render_template('about/about.html')

    @app.route('/account', methods=['GET', 'POST'])
    def account():
        if request.method == 'POST':
            if 'login' in request.form:
                # LOGIN logic
                email = request.form['email']
                password = request.form['password']
                user = User.query.filter_by(email=email).first()
                if user and bcrypt.check_password_hash(user.password, password):
                    login_user(user)
                    flash('Logged in successfully.', 'success')
                    return redirect(url_for('account'))
                else:
                    flash('Invalid login credentials.', 'danger')

            elif 'register' in request.form:
                # Registration logic
                username = request.form['username']
                email = request.form['email']
                password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

                if User.query.filter_by(email=email).first():
                    flash('Email already registered.', 'warning')
                    return redirect(url_for('account'))

                user = User(username=username, email=email, password=password)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash('Account created and logged in!', 'success')
                return redirect(url_for('account'))

        return render_template('account/account.html', user=current_user if current_user.is_authenticated else None)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('account'))