import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import CSRFProtect
from flask_bcrypt import Bcrypt
from forms import UserForm, RegistrationForm, LoginForm
from models import db, User
from sqlalchemy.exc import IntegrityError

app = Flask(__name__, instance_relative_config=True)

# ————— Configuration ————— #
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///' + os.path.join(app.instance_path, 'firstapp.db'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SECRET_KEY': os.environ.get('SECRET_KEY') or 'change-this!',
    'SESSION_COOKIE_SECURE': True,
    'SESSION_COOKIE_HTTPONLY': True,
    'SESSION_COOKIE_SAMESITE': 'Lax',
})
os.makedirs(app.instance_path, exist_ok=True)

# ————— Extensions ————— #
db.init_app(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

# ————— Handlers ————— #
@app.errorhandler(404)
def not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(e):
    app.logger.error(f"Server Error: {e}", exc_info=True)
    return render_template('errors/500.html'), 500

# ————— Routes ————— #
@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data, password='')
        db.session.add(user)
        db.session.commit()
        flash('User added successfully.', 'success')
        return redirect(url_for('index'))
    users = User.query.all()
    return render_template('index.html', form=form, users=users)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted.', 'info')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_u = User(name=form.name.data, email=form.email.data, password=pw_hash)
        db.session.add(new_u)
        try:
            db.session.commit()
            flash('Registration successful.', 'success')
            return redirect(url_for('login'))
        except IntegrityError:
            db.session.rollback()
            flash('Email already registered.', 'danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Logged in successfully.', 'success')
            return redirect(url_for('index'))
        flash('Invalid credentials.', 'danger')
    return render_template('login.html', form=form)

# ————— Init & Run ————— #
def init_db():
    db_path = os.path.join(app.instance_path, 'firstapp.db')
    if not os.path.exists(db_path):
        db.create_all()
    else:
        if not db.inspect(db.engine).get_table_names():
            db.create_all()

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=False)
