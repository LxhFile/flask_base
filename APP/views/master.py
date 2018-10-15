''''''
'''
==============================导入蓝本==========================================
'''
from flask import Blueprint, render_template

'''
==============================创建蓝本==========================================
一般变量名和蓝本名取一样
变量名 = Blueprint('蓝本名',__name__)
蓝本管理的作用是管理分类url，也就是说蓝本名的就是一个前缀  /蓝本名/url/
'''
'''
def __init__(self, name, import_name, static_folder=None,
             static_url_path=None, template_folder=None,
             url_prefix=None, subdomain=None, url_defaults=None,
             root_path=None):
'''
master = Blueprint('master', __name__)

# 要去views.__init__文件里注册蓝本

'''
==============================views编写=========================================
方法名不能和蓝本名一致，否者在views.__init__文件里导入蓝本的时候会发生错误，系统不知道该导入的是方法还是蓝本
就会提示：
    AttributeError: 'function' object has no attribute 'name'
'''


@master.route('/home/')
def master_q():
    return render_template('master/master.html')
