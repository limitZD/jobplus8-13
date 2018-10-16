from flask import Blueprint,render_template

company = Blueprint('company',__name__,url_prefix='/company')
 
@company.route('/')
def company_list():
    return render_template('company_list.html')

