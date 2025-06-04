import os, uuid
from cloudinary.uploader import upload as cloudinary_upload
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename
from app.models import User, Booking
from app.extensions import db, bcrypt
from datetime import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/account')

# Helper to check file extension - KR 25/05/2025
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


# Account route - login/register and user profile view - KR 25/05/2025
@auth_bp.route('/', methods=['GET', 'POST'])
def account():
    if request.method == 'POST':
        if 'login' in request.form:
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                # Redirect admins to the admin  - KR 29/05/2025
                if user.is_admin:
                    return redirect(url_for('auth.admin_dashboard'))
                return redirect(url_for('auth.account'))
            else:
                flash('Invalid login credentials.', 'danger')

        elif 'register' in request.form:
            username = request.form['username']
            email = request.form['email']
            password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            first_name = request.form['first_name']
            surname = request.form['surname']
            band_artist_name = request.form.get('band_artist_name')

            if User.query.filter_by(email=email).first():
                flash('Email already registered.', 'warning')
                return redirect(url_for('auth.account'))

            # Upload profile image to Cloudinary - KR 04/06/2025
            profile_image_url = None
            if 'profile_image' in request.files:
                file = request.files['profile_image']
                if file and allowed_file(file.filename):
                    result = cloudinary_upload(file, folder='profile_images')
                    profile_image_url = result['secure_url']

            user = User(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                surname=surname,
                band_artist_name=band_artist_name,
                profile_image=profile_image_url
            )

            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Account created and logged in!', 'success')

            if user.is_admin:
                return redirect(url_for('auth.admin_dashboard'))
            return redirect(url_for('auth.account'))

    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('auth.admin_dashboard'))

        now = datetime.now()
        bookings = current_user.bookings
        upcoming_bookings = [
            b for b in bookings if datetime.combine(b.date, b.start_time) >= now
        ]
        past_bookings = [
            b for b in bookings if datetime.combine(b.date, b.finish_time) < now
        ]

        return render_template(
            'account/account.html',
            user=current_user,
            upcoming_bookings=upcoming_bookings,
            past_bookings=past_bookings
        )

    return render_template('account/account.html')


# Admin dashboard route - KR 29/05/2025
@auth_bp.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('auth.account'))

    from sqlalchemy.orm import joinedload
    bookings = Booking.query.options(joinedload(Booking.user)) \
        .order_by(Booking.date.desc(), Booking.start_time).all()

    return render_template('account/admin_dashboard.html', user=current_user, bookings=bookings)


# Logout user - KR 25/05/2025
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.account'))


# Edit profile route - KR 25/05/2025
@auth_bp.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        current_user.username = request.form['username']
        current_user.first_name = request.form['first_name']
        current_user.surname = request.form['surname']
        band_name = request.form.get('band_artist_name')
        current_user.band_artist_name = band_name if band_name else None

        new_email = request.form['email']
        if new_email != current_user.email:
            if User.query.filter_by(email=new_email).first():
                flash('Email already in use.', 'danger')
                return redirect(url_for('auth.edit_profile'))
            current_user.email = new_email

        # Handle profile image upload via Cloudinary - KR 25/05/2025
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and allowed_file(file.filename):
                result = cloudinary_upload(file, folder='profile_images')
                current_user.profile_image = result['secure_url']

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('auth.account'))

    return render_template('account/edit_profile.html', user=current_user)
