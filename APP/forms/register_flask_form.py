''''''

'''
下载两个表单插件
pip install flask-wtf
pip install wtform
'''

'''
======================================导入插件中的方法============================================
'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

import re

'''
===========================================views================================================
'''
''''
 'BooleanField', 复选框
 'TextAreaField', 多文本
 'PasswordField', 密码
 'FileField', 文件
 'MultipleFileField', 多文件
 'HiddenField',  隐藏
 'SubmitField', 提交
  'TextField' 单

'''


# 注册表单方法，继承flask-wtf的Flaskform模块
class register_form(FlaskForm):
    # class StringField(Field):
    username = StringField(label='用户名',  # 标签
                           validators=[DataRequired(message='用户名不能为空'),
                                       ],  # 过滤器 , 可以放多个
                           render_kw={
                               'class': 'usernameClass'
                           }  # 标签属性 字典
                           )

    password = PasswordField(label='密码',
                             validators=[DataRequired(message='密码不能为空'),
                                         Length(min=6, max=16, message='请输入6-16位的密码'),
                                         ],
                             )

    repassword = PasswordField(label='请确认密码',
                               validators=[EqualTo('password', message='两次输入密码不相等')]
                               )

    email = StringField(label='邮箱',
                        validators=[Email(message='邮箱格式不正确')])

    submit = SubmitField(label='注册')

    # # 自定义表单验证 validate_+字段名
    # def validate_email(self,filder):
    #     # 验证方式
    #     emailRe = '[a-z0-9_]+@[a-z0-9]+\.[a-z]{2,4}'
    #     # I 是忽略大小写
    #     if not re.findall(emailRe,filder.data,re.I):
    #         # 如果不能匹配，抛出异常
    #         raise ValidationError('邮箱格式不正确')
