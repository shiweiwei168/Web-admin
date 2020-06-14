from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import Admin,Customer


@app.route('/')
@app.route('/index')
@login_required
def index():
    
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Admin(username=form.username.data, email=form.email.data, phone=form.phone.data,department=form.department.data, usertype=int(form.usertype.data))
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you registered a new user for the system!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/view')
@login_required
def view():
    customers = Customer.query.all()
    return render_template('view.html', title='view all customers', customers = customers)
