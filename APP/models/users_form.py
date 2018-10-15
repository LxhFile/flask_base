# -*- coding:utf-8 -*-
# @TIME     : 2018/09/05  00:38
# @AUTHOR   : LXH
# @FILE     : users_form.py

'''
导入extensions插件包的创建好的原始数据库模型对象 db = SQLAlchemy()
'''
from ..extensions import db

#创建数据表模型,  继承db.Model
class UserModels(db.Model):
    #设置个表名 默认是类名 默认的格式是：大写转小写，第二个单词后下划线隔开的
    #默认表名长这样 user_models  ，所以我们还是自定义一个表名
    __tablename__ = 'users'

    #主建  SQLAlchemy 中不会自动生成主键 ，得自己设置
    id = db.Column(db.Integer, primary_key=True, #一般设置为主键就会自动增长了，但我们为了以防万一，还算写上
                   autoincrement=True,  #自动增长
                   )
    username = db.Column(db.String(32), #一定要写长度
                         unique=True,  #唯一
                         )
    password = db.Column(db.String(64), #根据加密算法来设置长度
                         nullable=False,  #非空
                         )
    email = db.Column(db.String(32),)#邮箱32位够了

    sex = db.Column(db.Boolean, #性别可以用小数字 0 1 来代表，也可以用booler值来设置
                    default=True, #默认选中男
                    )

'''
建好表模型后，先去__init__.py中初始化导入
'''