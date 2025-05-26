from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/home')
def home():
    return render_template('home/home.html')

@main_bp.route('/services')
def services():
    return render_template('services/services.html')

@main_bp.route('/about')
def about():
    return render_template('about/about.html')

@main_bp.route('/booking', methods=['GET', 'POST'])
@login_required
def book():
    if request.method == 'POST':
        # Process form submission - KR 26/05/2025
        flash("Booking submitted successfully!", "success")
        return redirect(url_for('main.book'))

    return render_template('book/book.html', user=current_user)