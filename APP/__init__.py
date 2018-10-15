''''''

'''
===========================================导入包,导入即加载===========================================
'''
# 导入flask
from flask import Flask

#导入config字典
from .config import config

# # 加载配置环境(类)   错
# from .config import Config

# 加载扩展插件(方法)
from .extensions import config_extensions

# 导入蓝本，激活蓝本
from .views import config_blueprint

# 导入数据表模型models, 加*之后就不需要每个新表都动了,写好后在manage.py  main这里测试一下
from .models import *

'''
=====================================封装初始化方法========================================
'''


# 封装初始化方法
def create_app(config_name):
    # 实例化一个app
    app = Flask(__name__)
    '''
    class Flask(_PackageBoundObject)
     从对象（app）中  -加载配置文件  对象用的 object
    config是app对象中self.config的方法
    from_object是class Config(dict) 中的方法
     config.get就是我们写的字典
    '''
    app.config.from_object(config.get(config_name))

    '''
     加载额外配置
     config是配置字典.get是获得字典中的值，传入配置名(形参)config_name
     .(被设置的静态方法)init_app(app(这个是实例化的Flask对对象))
    '''
    config.get(config_name).init_app(app)

    '''
     加载扩展
     config_extensions是extensions中的封装扩展的方法，app是实例化的Flask对象
    '''
    config_extensions(app)

    '''
    激活蓝本
    '''
    config_blueprint(app)

    # 返回一个被加载好的app对象
    return app

# 要去manage.py里管里app.init初始化方法
