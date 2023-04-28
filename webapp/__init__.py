from flask import Flask, jsonify, request
from flask import render_template
import os
import json

main_navigation = {
    'Home': '/home',
    'Logout': '/home',
}

sidebar_navigation = {
    'Dashboard': '/home',
    'Kanban': '/home',
    'Inbox': '/home',
    'Users': '/home',
    'Products': '/home',
    'Support': '/home',
}
searchfilter = [
    {'firstname': '', 'label': 'Firstname'},
    {'lastname': '', 'label': 'Lirstname'},
    {'email': '', 'label': 'E-mail'},
    {'dateofbirth': '', 'label': 'Date of birth'},
]
absolute_path = os.path.dirname(__file__)
relative_path = "data\sample.json"
full_path = os.path.join(absolute_path, relative_path)
fi = open(full_path, 'r')
sample_data = json.load(fi)
fi.close()

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template(
            "home.html",
            main_navigation = main_navigation,
            sidebar_navigation = sidebar_navigation,
            searchfilter = searchfilter,
            table_headers = sample_data[0]['headers'],
            table_data = sample_data[0]['data']
        )
    @app.route('/api/sample', methods=['GET'])
    def sampledata():
        if(request.method == 'GET'):
            return jsonify(sample_data)
    return app