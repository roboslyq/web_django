#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
完全可以把信息收集客户端做成Windows和Linux两个不同版本。
"""

import os
import sys
from django_app.cmdb.Client.core import handler

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
