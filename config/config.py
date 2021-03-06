#!/usr/bin/env python 
# -*- encoding: utf-8 -*- 
"""
@Author  : zhoutao
@License : (C) Copyright 2013-2017, China University of Petroleum
@Contact : zhoutao@s.upc.edu.cn
@Software: PyCharm
@File    : config.py 
@Time    : 2020/3/21 21:42 
@Desc    : 编译项目的配置文件
"""
# 排除文件夹不编译
exclude = ["venv", "__pycache__", ".idea", "data"]
# 查找文件的后缀
build_file_suffix = [".py"]
# 删除中间文件
middle_suffix = [".c", ".o"]
# python版本
python_version = 3
# 源文件夹
src = "/home/chase/cython/test"
# 编译目标文件夹
destination = "/home/chase/cython/test/build"
# 缓存文件夹
temp = "/home/chase/cython/test/temp"
