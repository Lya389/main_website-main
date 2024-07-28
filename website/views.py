from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user
from .model import Post, User, Like
from .import db

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", user=current_user)

@views.route("/choice")
def choice():
    return render_template("choice.html", user=current_user)

@views.route("/updates")
def updates():
    posts = Post.query.all()
    return render_template("updates.html", user=current_user, posts=posts)

@views.route("/admin")
def admin():
    posts = Post.query.all()
    return render_template("admin/index.html", user=current_user, posts=posts)

@views.route("/create", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')
        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created', category='success')
            return redirect(url_for('views.updates'))
    return render_template('create.html', user=current_user)
