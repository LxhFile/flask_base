''''''
'''
=======================================导入蓝本=================================================
'''
from flask import Blueprint, render_template

'''
======================================创建蓝本对象=============================================
'''
client = Blueprint('client', __name__)

# 要去views.__init__文件里注册蓝本

'''
======================================views编写===============================================
方法名不能和蓝本名一致，否者在views.__init__文件里导入蓝本的时候会发生错误，系统不知道该导入的是方法还是蓝本
就会提示：
    AttributeError: 'function' object has no attribute 'name'
'''


# 客人界面
@client.route('/home/')
def client_q():
    return render_template('client/client.html')
