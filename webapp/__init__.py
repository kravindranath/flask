from flask import Flask 
from flask import render_template

main_navigation = {
    'Home': '/home',
    'Login': '/home',
    'Contact us': '/home',
}

sidebar_navigation = {
    'Dashboard': '/home',
    'Kanban': '/home',
    'Inbox': '/home',
    'Users': '/home',
    'Products': '/home',
    'Sign': '/home',
    'Sign': '/home',
}

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def home():
        return render_template(
            "home.html",
            main_navigation = main_navigation,
            sidebar_navigation = sidebar_navigation,
        )

    return app