from flask import render_template, session, request, redirect, url_for, flash

from loja import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User
import os


@app.route('/admin')
def admin():
    if 'email' not in session:
        return redirect(url_for('login'))
    return render_template('admin/index.html', title="Pagina adminstrativa")

@app.route('/registrar', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.username.data} por registrar', 'success')
        
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title="Pagina de registro")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Seja bem vindo {form.email.data}', 'success')
            return redirect(request.args.get('next')or url_for('registrar'))
        else:
            flash('Não foi possivel acessar o sistema')            
    return render_template('admin/login.html', form=form, title="Pagina login")
    