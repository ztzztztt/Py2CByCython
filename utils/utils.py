#!/usr/bin/env python 
# -*- encoding: utf-8 -*- 
"""
@Author  : zhoutao
@License : (C) Copyright 2013-2017, China University of Petroleum
@Contact : zhoutao@s.upc.edu.cn
@Software: PyCharm
@File    : utils.py 
@Time    : 2020/3/21 12:43 
@Desc    : 编译项目的工具文件
"""
import os
from shutil import rmtree
from config import config
from distutils.core import setup
from Cython.Build import cythonize

__py_file_list = []
__middle_file_list = []


def delete_temp():
    """
    删除temp缓存文件
    :return:
    """
    if os.path.exists(config.temp):
        rmtree(config.temp)
    pass


def delete_middle_file():
    """
    删除编译过程中的中间文件
    :return:
    """
    middle_file_list = __delete_middle_file(config.src)
    if middle_file_list and middle_file_list.__len__() != 0:
        for file in middle_file_list:
            if os.path.exists(file):
                os.remove(file)
    pass


def __delete_middle_file(root_dir):
    """
    查找编译的中间文件，例如.o,.c文件等
    :param root_dir: 查找文件根路径
    :return:
    """
    dir_file_list = os.listdir(root_dir)
    # 遍历每一的文件列表
    for dir_or_file_name in dir_file_list:
        # 获取该文件的全路经
        child_path = os.path.join(root_dir, dir_or_file_name)
        # 如果该路径是文件夹
        if os.path.isdir(child_path) and dir_or_file_name not in config.exclude:
            # 递归执行此函数
            __delete_middle_file(child_path)
        # 获取文件名的后缀
        middle_file_temp = os.path.splitext(dir_or_file_name)[-1]
        # 判断是否需要删除
        if middle_file_temp in config.middle_suffix:
            __middle_file_list.append(child_path)
    return __middle_file_list
    pass


def generate_setup_compiler(file_path):
    """
    传入需要编译的文件，完成编译。并且放到指定的文件中
    :param file_path: 需要编译的文件
    :return:
    """
    # 获取对应文件的存放文件夹
    base_dir = os.path.dirname(file_path)
    # 转义路径，防止不同系统上不匹配的问题
    src_dir = os.path.join(config.src, "")
    # 获取项目的层次结构
    child_dir_list = base_dir.split(src_dir)
    if child_dir_list.__len__() >= 2:
        child_dir = child_dir_list[1]
    else:
        return
    build_path = os.path.join(config.destination, child_dir)
    setup(
            ext_modules=cythonize(file_path, language_level=config.python_version),
            script_args=[
                "build_ext",
                "-b", build_path,
                "-t", config.temp
            ]
        )
    pass


def get_py_list_from_path(root_dir):
    """
    获取路径下的文件列表
    :param root_dir: 输入的根路径
    :return: 所有python文件的路径
    """
    # 获取对应路径下的文件列表
    dir_file_list = os.listdir(root_dir)
    # 遍历每一的文件列表
    for dir_or_file_name in dir_file_list:
        # 获取该文件的全路经
        child_path = os.path.join(root_dir, dir_or_file_name)
        # 如果该路径是文件夹
        if os.path.isdir(child_path) and dir_or_file_name not in config.exclude:
            # 递归执行此函数
            get_py_list_from_path(child_path)
        # 获取文件的后缀名
        build_file_suffix = os.path.splitext(dir_or_file_name)[-1]
        # 判断是否需要编译
        if build_file_suffix in config.build_file_suffix:
            __py_file_list.append(child_path)
    return __py_file_list
