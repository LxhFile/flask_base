# 配置文件设置

import os

# 找到项目根目录
'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
# /home/lxh/flask_demo/APP
'''
'''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
/home/lxh/flask_demo
'''
'''
os.path.dirname(文件绝对路径)  获得当前路径的文件夹名，相当于上一层的路径
os.path.abspath(文件名)当前文件名用__file__来代替
我们要给BASE_DIR存的是项目根目录
'''

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 配置基类,继承object
class Config(object):
    # 通用配置 必须大写
    # 密钥 每次调用随机生成32位的密钥  , 只有用到session的时候才用启用，用session之前先要进行redis的开启
    SECRET_KEY = os.urandom(32)
    # SECRET_KEY = '123456'

    # 留个额外配置的封装方法
    '''
    将函数转化为静态方法，并可以在类中调用 例如：Config.方法名()
                        或者在实例中调用 例如: Config().方法名()  这个实例会被忽略，除了他它的类外
    '''

    @staticmethod
    def init_app(app):  # 因为预留坑是为了给app用的，所以形参给个app的名字,暂时还没添加其他类型的配置所以就写个pass
        pass


'''
==================================环境配置==================================================
'''


# 开发环境 , 继承通配设置
class DevelopmentConfig(Config):
    ''''''
    '''
    配置数据库环境
    mysql 配置
    mysql+驱动(驱动:python3的是pymysql   python2的是mysqldb) ://用户名:密码@host:port/数据库名
    数据库必须三干净的
    '''
    #忽略警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1806lxh@172.20.10.8:3306/flask_demo'

    #数据提交自动保存
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  #配置完成后去到manage里添加extensions的db命令


    '''
    sqlite 配置
    'sqlite:/// + 路径 + 数据库名'
    '''
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'flask.sqlite')


# 测试环境, 继承通配设置
class TestConfig(Config):
    pass


# 发布环境 ， 继承通配设置
class ProductConfig(Config):
    pass


'''
=========================================通配字典,用于找到环境=======================================
'''
# 默认是开发环境
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig,
}
