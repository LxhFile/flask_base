''''''
'''
=======================================管理文件=================================================
'''
'''
================================导入app.__init__ 初始化方法=====================================
'''
from APP import create_app    #__init__是文件运行的入口


'''
==================================其他包的导入==============================================
'''
import os                           #获取环境变量
from flask_script import Manager  #导入命令脚本控制启动app
from APP.extensions import db   #导入实例化 类 db 这个导入是为了测试

from flask_script import prompt_bool  #用与数据库操作的,
#  在终端操作时给与对话框提示，根据用户输入的y/n，返回True/False

from flask_migrate import MigrateCommand  #pip install flask-migrate
  #使用命令向__init__初始化，生成迁移，执行迁移的命令都在里面

'''
======================================选择环境================================================
'''
'''
os.getenv('FLASK_ENV')
""获取一个环境变量，如果它不存在，返回None。
可选的第二个参数可以指定另一个默认值。
key, default和结果是str 输入也是str"""
'''
config_name = os.getenv('FLASK_ENV') or 'default'

# Terminal 命令 export FLASK_ENV=default

'''
=====================================创建__init__完后的app====================================
'''

app = create_app(config_name)


'''
=====================================创建管理app对象=========================================
'''

manager = Manager(app)

'''
==================================向manager添加一条数据库命令==========================================
'''
# 向manager添加一条db命令，参数是MigrateCmmand
manager.add_command('db',MigrateCommand)
'''
命令有：
    manage.py: error: invalid choice: 'help' (choose from 'db', 'shell', 'runserver')
    python manage.py db  --  查看有什么命令方法 -- init初始化 创建migration file
                         --  migrate -- 生成迁移表
                         --  upgrade -- 执行迁移表
    python manage.py runserver --运行 可加参数 --  -r自动重启  -h host  -p port  --threaded开启多线程 
    还有很多...
'''
#添加命令后,去models包创建表模型
'''
======================================run测试================================================
'''
@app.route('/')
def hello():
    return 'ok'

#添加manager方法
#添加后变成了 (choose from 'db', 'create', 'shell', 'runserver')
@manager.command  #不加括号,导入的是值
def create():
    '''
    调用方法，创建表
    :return: tabel创建成功
    '''
    db.create_all()
    return 'tabel创建成功'

#添加manager方法
#添加后变成了 (choose from 'db', 'create', 'drop', 'shell', 'runserver')
@manager.command
def drop():
    '''
    调用删除表方法,在删除前用prompt_bool做程序进行的前一步,自动询问是否删除, 在控制台要输入 y/n
    :return:
    '''
    if prompt_bool('是否删除表'):
        #如果输入y
        db.drop_all() #删除所有表
    else:
        #输入n
        return '感谢放过'
    return '删库跑路'

if __name__ == '__main__':
    manager.run()

'''
端口错误，地址已经被占用
OSError: [Errno 98] Address already in use
换个端口就能跑
'''
