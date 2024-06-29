from flask import Blueprint, request, redirect, url_for, render_template
from ..model.user import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def list_users():
    users = User.get_all()
    return render_template('user/index.html', users=users)

@user_bp.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        User.create(name, email)
        return redirect(url_for('user.list_users'))
    return render_template('user/create.html')