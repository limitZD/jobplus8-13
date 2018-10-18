from flask import Blueprint,render_template,flash,redirect,url_for
from jobplus.forms import UserRegisterForm,CompanyRegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required
from jobplus.models import User

front = Blueprint('front',__name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/user_register',methods=['POST','GET'])
def user_register():
    forms = UserRegisterForm()
    if forms.validate_on_submit():
        forms.create_user()
        flash('注册成功，请登录！','success')
        return redirect(url_for('.login'))
    return render_template('user_register.html',forms=forms)

@front.route('/comp_register',methods=['POST','GET'])
def comp_register():
    forms = CompanyRegisterForm()
    if forms.validate_on_submit():
        forms.create_company()
        flash('注册成功，请登录！','success')
        return redirect(url_for('.login'))
    return render_template('comp_register.html',forms = forms)

@front.route('/login',methods=['GET','POST'])
def login():
    forms = LoginForm()
    if forms.validate_on_submit():
        user = User.query.filter_by(email=forms.email.data).first()
        
        if user.is_company():
            login_user(user,forms.remember_me.data)
            return redirect(url_for('company.profile'))
        elif user.is_admin():
            login_user(user,forms.remember_me.data)
            return redirect(url_for('admin.profile'))
        else:           
            login_user(user,forms.remember_me.data)
            return redirect(url_for('user.profile'))
    return render_template('login.html',forms = forms)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('tui chu','success')
    return redirect(url_for('.index'))
