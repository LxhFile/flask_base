''''''
'''
================================导入包=======================================
'''
from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, Length


class login_form(FlaskForm):
    # 用户名
    username = StringField('用户名', validators=[InputRequired('用户名不能为空')])

    # 密码
    password = PasswordField('密码', validators=[InputRequired('密码不能为空')])

    # 验证码
    code = StringField('验证码', validators=[InputRequired('验证码不能为空')])

    # 登陆
    button = SubmitField('登陆')
