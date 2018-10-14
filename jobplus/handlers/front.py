from flask import Blueprint,render_template
from jobplus.forms import UserRegisterForm,CompanyRegisterForm,LoginForm

front = Blueprint('front',__name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/user_register')
def user_register():
    forms = UserRegisterForm()
    return render_template('user_register.html',forms=forms)

@front.route('/comp_register')
def comp_register():
    forms = CompanyRegisterForm()
    return render_template('comp_register.html',forms = forms)

@front.route('/login')
def login():
    forms = LoginForm()
    return render_template('login.html',forms = forms)



