from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

"""
Note that in the above code, some arguments are aspeficied when creating a blueprint object.
The first argument, "site", is the Blueprint name as a string,
which is used by flask's routing mechanism.
The second argument __name__ is the Blueprint's import name, 
which Flask uses to locate the Blueprint's resources.
The third is telling Flask where to find the HTML to render.
"""

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')