import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from app.models import User
from app.extensions import db, bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/account')

# Helper to check file extension - KR 25/05/2025
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@auth_bp.route('/', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        if 'login' in request.form:
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
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

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.account'))

@auth_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.first_name = request.form['first_name']
        current_user.surname = request.form['surname']

        new_email = request.form['email']
        if new_email != current_user.email:
            if User.query.filter_by(email=new_email).first():
                flash('Email already in use.', 'danger')
                return redirect(url_for('auth.edit_profile'))
            current_user.email = new_email

        # Handle profile image upload - KR 25/05/2025
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                current_user.profile_image = filename

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('auth.account'))

    return render_template('account/edit_profile.html', user=current_user)
    

