from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Booking
from datetime import datetime, date
from app.extensions import db

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
        booking_date_str = request.form['date']
        start_time_str = request.form['start_time']
        finish_time_str = request.form['finish_time']
        studio = request.form['studio']
        notes = request.form.get('notes', '')

        try:
            booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d").date()
            start_time = datetime.strptime(start_time_str, "%H:%M").time()
            finish_time = datetime.strptime(finish_time_str, "%H:%M").time()
        except ValueError:
            flash("Please enter valid date and time values.", "danger")
            return redirect(url_for('main.book'))

        if finish_time <= start_time:
            flash("Finish time must be after start time.", "warning")
            return redirect(url_for('main.book'))

        existing = Booking.query.filter(
            Booking.date == booking_date,
            Booking.studio == studio,
            Booking.start_time < finish_time,
            Booking.finish_time > start_time
        ).first()

        if existing:
            flash("This time slot is already booked for the selected studio.", "warning")
            return redirect(url_for('main.book'))

        new_booking = Booking(
            user_id=current_user.id,
            date=booking_date,
            start_time=start_time,
            finish_time=finish_time,
            studio=studio,
            notes=notes
        )
        db.session.add(new_booking)
        db.session.commit()

        flash("Booking created successfully!", "success")
        return redirect(url_for('main.book'))

    return render_template('book/book.html', user=current_user, date=date)

@main_bp.route('/booking/<int:booking_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('auth.account'))

    if request.method == 'POST':
        booking.date = datetime.strptime(request.form['date'], "%Y-%m-%d").date()
        booking.start_time = datetime.strptime(request.form['start_time'], "%H:%M").time()
        booking.finish_time = datetime.strptime(request.form['finish_time'], "%H:%M").time()
        booking.studio = request.form['studio']
        booking.notes = request.form.get('notes', '')

        db.session.commit()
        flash("Booking updated successfully!", "success")
        return redirect(url_for('auth.account'))

    return render_template('book/edit_booking.html', booking=booking)

@main_bp.route('/booking/<int:booking_id>/delete', methods=['POST'])
@login_required
def delete_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)
    if booking.user_id != current_user.id:
        flash("Unauthorized action.", "danger")
        return redirect(url_for('auth.account'))

    db.session.delete(booking)
    db.session.commit()
    flash("Booking deleted.", "info")
    return redirect(url_for('auth.account'))