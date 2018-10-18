from flask import Blueprint,render_template,flash,redirect,url_for
from jobplus.forms import UserProfileForm
from flask_login import current_user,login_required

user = Blueprint('user',__name__,url_prefix='/user')

@user.route('/profile',methods=['GET','POST'])
@login_required
def profile():
    form = UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.updated_profile(current_user)
        flash('上传成功','success')
        return redirect(url_for('front.index'))
    return render_template('user_prof.html',form = form)


