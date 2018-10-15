from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import DataRequired,Length,Email,EqualTo
from .models import db,User

class UserRegisterForm(FlaskForm):
    username = StringField("用户名",validators=[DataRequired(),Length(4,24)])
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('提交')
    
    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_name(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("此用户名己存在！")

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
             raise ValidationError("此邮箱己存在！")
              

class CompanyRegisterForm(FlaskForm):
    username = StringField("企业名称",validators=[DataRequired(),Length(4,24)])
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
    repeat_password = PasswordField('重复密码',validators=[DataRequired(),EqualTo(password)])
    submit = SubmitField('提交')

    def create_company(self):
         user = User()
         user.username = self.username.data
         user.email = self.email.data
         user.password = self.password.data
         user.role = 20
         db.session.add(user)
         db.session.commit()
         return user

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')
 
    def validate_email(self,field):
        if not User.query.filter_by(email==field.data).first():
            raise ValidationError('邮箱错误!')

    def validate_password(self,field):
        user = User.query.filter_by(password==field.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误!')

