''''''
'''
====================================初始化,注册蓝本===============================================
'''

'''
=================================导入views.py文件的蓝本对象=======================================
'''
from .master import master
from .client import client
from .register import register
from .login import login
'''
==========================写入二维蓝本元组（蓝本对象名,‘蓝本前缀’）================================
变量名用大写,行规
用元组,是因为元组数据不可变
'''
BASE_BLUEPRINT = (
    (master, '/master'),
    (client, '/client'),
    (register, '/register'),
    (login, '/login'),

)

'''
====================================封装蓝本注册方法============================================
'''


def config_blueprint(app):
    # 这样写是原始的方法
    # app.register_blueprint(user, url_prefix='/user')
    # app.register_blueprint(teacher, url_prefix='/teacher')

    # 这也是二维元组的写法
    for blueprint_name, url_prefix in BASE_BLUEPRINT:
                                                        # url_prefix= 用于定义url前缀
        app.register_blueprint(blueprint=blueprint_name, url_prefix=url_prefix)

# 要去app.__init__里去初始化导入
