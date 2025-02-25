from flask import Blueprint, render_template, request, redirect
from .forms import LoginForm, RegisterForm
from .account_service import user_add_api, user_login_validate, user_get, password_hash
from flask_login import login_user, logout_user, login_required



auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])  
def login():  
    form = LoginForm()
    if request.method == 'POST':
        user_data = request.form
        result = user_login_validate(user_data['username'], user_data['password'])
        if result == "success":
            user = user_get(user_data['username'])
            login_user(user)  
            return redirect('/blog')
        else:
            return render_template('login.html', form=LoginForm(), errors="Username or Password is incorrect")
    return render_template('login.html', form=LoginForm())

@auth.route('/register', methods=['GET', 'POST'])  
def register():  
    form = RegisterForm()
    if request.method == 'POST':
        user_data = request.form
        if user_data['username'] != '' and user_data['password'] != '':
            result = user_add_api(user_data['username'], password_hash(user_data['password']))
            if result == "success":
                return redirect('/login')
            else:
                return render_template('register.html', form=RegisterForm(), errors="Username already exists")
        else:
            return render_template('register.html', form=RegisterForm(), errors="Username or Password is empty")
    return render_template('register.html', form=RegisterForm())


@auth.route('/logout')  
@login_required
def logout():
    logout_user()
    return "You are logged out successfully , please login again <a href='/login'>Login</a>"

