from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class UserRegisterForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired(),Length(4,24)])
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('提交')


class CompanyRegisterForm(FlaskForm):
    username = StringField("企业名称",validators=[DataRequired(),Length(4,24)])
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('提交')


class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')



