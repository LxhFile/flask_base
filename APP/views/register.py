''''''

'''
==============================================创建蓝本============================================
'''
from flask import Blueprint

register = Blueprint('register', __name__)

# 去init注册蓝本

'''
===============================================导入其他模块======================================
'''
from flask import render_template, request, session

'''
千万要注意这个调用之前要在form包里面的__init__py文件初始化，
不然无法运行，会报错，而且错误看不出来
错误信息:
RuntimeError: Working outside of application context.
 
This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.
'''
from APP.forms import register_form

'''
=============================================views===============================================
'''


@register.route('/q/')
def re_q():
    return render_template('master/master.html')

# flask-wtf
@register.route('/register/', methods=['GET', 'POST'])
def register_function():
    # print('进到方法里了')
    # 创建表单对象,实例化
    register_object = register_form()
    # 判断post提交
    if request.method == 'POST':   #注意不能多空格，多了空格就进不来了
        # 验证表单数据
        # print('进入post')

        """
        Consider the form submitted if there is an active request and
            the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        """
        if register_object.validate_on_submit():  # 如果表单对象提交了 那么我们就验证 验证才能在前台提示信息
            # print('进入验证')
            # pass
            # 获取数据
            # wtf.data 获取用户名文本框提交的信息数据
            username = register_object.username.data
            # 清空文本框的值
            register_object.username.data = ''
            # 查找session中是否存在上一个用户名数据，不存在就为空
            last_user = session.get('username') or None
            # 判断上一个用户名是否存在并且属于同一个用户名
            if last_user and username == last_user:
                # 跳转回注册页面 返回清空了的用户对象
                return render_template('form/register.html', form=register_object, message='重复提交')
            else:  # 是第一次提交就保存到session里，目前暂时存在session里
                # print('进入session')
                session['username'] = username
            # 成功后跳转 返回清空了的用户对象

            # print('成功跳转前')
            return render_template('success/success.html', form=register_object, message='ok')

    # print('进入get')
    # 如果是get请求，着跳转本身 返回清空了的用户对象
    return render_template('form/register.html', form=register_object)



#url快速生成表单
@register.route('/register_quick/', methods=['GET', 'POST'])
def register_quick():
    # print('进到方法里了')
    # 创建表单对象,实例化
    register_object = register_form()
    # 判断post提交
    if request.method == 'POST':   #注意不能多空格，多了空格就进不来了
        # 验证表单数据
        # print('进入post')

        """
        Consider the form submitted if there is an active request and
            the method is ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        """
        if register_object.validate_on_submit():  # 如果表单对象提交了 那么我们就验证 验证才能在前台提示信息
            # print('进入验证')
            # pass
            # 获取数据
            # wtf.data 获取用户名文本框提交的信息数据
            username = register_object.username.data
            # 清空文本框的值
            register_object.username.data = ''
            # 查找session中是否存在上一个用户名数据，不存在就为空
            last_user = session.get('username') or None
            # 判断上一个用户名是否存在并且属于同一个用户名
            if last_user and username == last_user:
                # 跳转回注册页面 返回清空了的用户对象
                return render_template('form/register_quick_form.html', form=register_object, message='重复提交')
            else:  # 是第一次提交就保存到session里，目前暂时存在session里
                # print('进入session')
                session['username'] = username
            # 成功后跳转 返回清空了的用户对象

            # print('成功跳转前')
            return render_template('success/success.html', form=register_object, message='ok')

    # print('进入get')
    # 如果是get请求，着跳转本身 返回清空了的用户对象
    return render_template('form/register_quick_form.html', form=register_object)