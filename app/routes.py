from flask import render_template, request, redirect, url_for, session, flash, jsonify

def register_routes(app):
    @app.route('/')
    def home():
        return render_template('home.html') 

    @app.route('/services')
    def services():
        return render_template('services.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')
    
    @app.route('/book')
    def book():
        return render_template('book.html')