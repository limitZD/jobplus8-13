from flask import Blueprint,render_template

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/profile')
def profile():
    return render_template('comp_prof.html')
