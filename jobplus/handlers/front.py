from flask import Blueprint,render_template,flash,redirect,url_for
from jobplus.forms import UserRegisterForm,CompanyRegisterForm,LoginForm


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

@front.route('/login')
def login():
    forms = LoginForm()
    return render_template('login.html',forms = forms)



