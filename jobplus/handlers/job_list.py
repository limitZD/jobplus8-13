from flask import Blueprint,render_template

job = Blueprint('job',__name__,url_prefix='/job')

@job.route('/')
def job_list():
    return render_template('job_list.html')
