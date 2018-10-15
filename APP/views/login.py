# 创建蓝本

from flask import Blueprint, render_template, request
import hashlib

# 创建蓝本对象


login = Blueprint('login', __name__)

from APP.forms import login_form


# 创建views方法

@login.route('/login/', methods=['GET', 'POST'])
def login_flask_wtf():
    # 创建对象
    form = login_form()

    if request.method == 'post':  # post提交
        if form.validate_on_submit():  # 提交前验证
            pass

    return render_template('form/login.html', form=form)
