from flask import Blueprint, render_template, request, redirect, url_for, flash
from drone_inventory.forms import UserLoginForm
from ..models import User
from flask_login import login_user, logout_user


auth = Blueprint('auth', __name__, template_folder = 'auth_templates')

@auth.route('/signup', methods = ['GET', 'POST'] )
def signup():
    form = UserLoginForm()
    try: 
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            password = form.password.data

            user = User(email, first_name, last_name, password)
            
            user.save_to_db()
            return redirect(url_for('auth.signin'))
            
        

    except: 
        raise Exception('Invalid Form Data: Please check your form')

    return render_template('signup.html', form=form)


@auth.route('/signin', methods = ['GET', 'POST'])
def signin():
    form = UserLoginForm()

    if request.method == 'POST':
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email = email).first()
        if user:
            if user.check_password(password):
                login_user(user)
                return redirect(url_for('site.home'))
            else:
                print("incorrect password")
        else: 
            print('information not found')

    return render_template('signin.html', form=form)
@auth.route('/logout', methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.signin'))


