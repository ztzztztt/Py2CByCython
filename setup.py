#!/usr/bin/env python 
# -*- encoding: utf-8 -*- 
"""
@Author  : zhoutao
@License : (C) Copyright 2013-2017, China University of Petroleum
@Contact : zhoutao@s.upc.edu.cn
@Software: PyCharm
@File    : setup.py
@Time    : 2020/3/21 12:20 
@Desc    : 编译项目的入口文件
"""
from config import config
from utils.utils import get_py_list_from_path, \
    generate_setup_compiler, delete_temp, delete_middle_file

if __name__ == "__main__":
    py_list = get_py_list_from_path(config.src)
    for py_file in py_list:
        generate_setup_compiler(py_file)
    delete_temp()
    delete_middle_file()
    pass
