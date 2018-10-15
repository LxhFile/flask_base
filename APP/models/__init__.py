# -*- coding:utf-8 -*-
# @TIME     : 2018/09/05  00:38
# @AUTHOR   : LXH
# @FILE     : __init__.py.py  初始化文件

#初始化表模型

from .users_form import UserModels

#初始化导入后，去app.__init.py__中加入初始化一下，但不需要封装方法（不用安装），加 × 星号
#之后的新表模型都不需要再动app.__init__.py了
#要使用表给表添加数据就去 views中写