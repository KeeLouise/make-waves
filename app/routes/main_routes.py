from flask import Blueprint, render_template

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