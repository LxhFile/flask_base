
'''扩展文件'''
'''
===================================导入插件==============================================
'''
from flask_moment import Moment          #pip install flask-moment
from flask_bootstrap import Bootstrap    #pip install flask-bootstrap
from flask_session import Session        #pip install flask-session   一般要开发的时候才发布 ， 如果要用也就是要启动redis
from flask_sqlalchemy import SQLAlchemy  #pip install flask-sqlalchemy  数据库的根数据库模型就是 sqlalchemy


'''
====================================实例化对象===========================================
'''
moment = Moment()
bootstrap = Bootstrap()
# se = Session()   #用session才会需要配置密钥
db = SQLAlchemy()
'''
session这个是要发的时候使用的要 启动redis
'''
'''
====================================封装扩展方法=========================================
'''

def config_extensions(app):  #都是用于app初始化的所以给个形参app
    #把插件安装到app中
    # class Moment(object) 中的 init_app方法
    moment.init_app(app)

    #class Bootstrap(object) 中的 init_app方法
    bootstrap.init_app(app)

    #class Session(object)  中的  init_app方法
    # se.init_app(app)

    # class SQLAlchemy(object): 中的 init_app方法
    db.init_app(app)    #安装完app之后要去config开发环境配置里，把python3 的pymysql给设置一下帐号密码  ; python2的是 mysqldb