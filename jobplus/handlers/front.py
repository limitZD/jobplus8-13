from flask import Blueprint,render_template

front = Blueprint('front',__name__)

@front.route('/')
def index():
    return render_template('index.html')

@front.route('/user_register')
def user_register():
    return render_template('user_register.html')

@front.route('/comp_register')
def comp_register():
    return render_template('comp_register.html')

@front.route('/login')
def login():
    return render_template('login.html')
