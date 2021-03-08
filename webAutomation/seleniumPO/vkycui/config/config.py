"""
@Time:  2021/3/2
@Author:chenzhe

"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
读取配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
import os
import platform

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 返回当前文件saaswebui的绝对路径
config_file = os.path.join(base_path, 'config', 'configurl.yml')
data_path = os.path.join(base_path, 'data', 'test_data.xls')
driver_path = os.path.join(base_path, 'config', 'chromedriver.exe') if "Windows" == platform.system() else \
    os.path.join(base_path, 'config', 'chromedriver')
log_path = os.path.join(base_path, 'result/log')
report_path = os.path.join(base_path, 'result/report')
photo_path = os.path.join(base_path, 'data', 'ocr.jpg')
key_file = os.path.join(base_path, 'config', 'id_rsa')

# 默认浏览器

# ①界面浏览器
browser = 'chrome'

# ②无头浏览器
# browser = 'headless_chrome'

