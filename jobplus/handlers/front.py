<<<<<<< HEAD
from flask import Blueprint,render_template,flash,redirect,url_for
from jobplus.forms import UserRegisterForm,CompanyRegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required
from jobplus.models import User
=======
from flask import Blueprint, render_template
from jobplus.models import Job, Company,User
from jobplus.forms import UserregisterForm,CompanyregisterForm,LoginForm
from flask import flash
from flask_login import login_user,logout_user,login_required
from flask import redirect,url_for

>>>>>>> upstream/master

front = Blueprint('front',__name__)

@front.route('/')
def index():
<<<<<<< HEAD
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
=======
    job = Job.query.all()
    company = Company.query.all()
    return render_template('index.html', job=job, company=company)

@front.route('/userregister',methods=['GET','POST'])
def userregister():
    form = UserregisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功,请登录!','success')
        return redirect(url_for('.login'))
    return render_template('userregister.html',form=form)

@front.route('/companyregister',methods=['GET','POST'])
def companyregister():
    form = CompanyregisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('注册成功，请登录!','success')
        return redirect(url_for('.login'))
    return render_template('companyregister.html',form=form)

@front.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user,form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html',form=form)
>>>>>>> upstream/master

@front.route('/logout')
@login_required
def logout():
    logout_user()
<<<<<<< HEAD
    flash('tui chu','success')
=======
    flash('你已退出登录','success')
>>>>>>> upstream/master
    return redirect(url_for('.index'))
