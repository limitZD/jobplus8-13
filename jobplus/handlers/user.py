from flask import Blueprint,render_template

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/profile')
def profile():
    return render_template('user_prof.html')


