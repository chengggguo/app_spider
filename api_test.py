#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: dou_yin.py 
@time: 5/14/19 09:16 
@description：抖音自动化运营
"""
# testestestest

from utils.baidu_utils import *
import time
from datetime import datetime
import shutil


print("testing")



if __name__ == '__main__':

    access_token = get_access_token()
    print("in the loop")



            # 人脸识别
    recognite_result = analysis_image(parse_image_pic("testImage1.jpg", TYPE_IMAGE_LOCAL, access_token))




            # 这是一个美女
    if recognite_result:

        print('识别到视频含有旗帜，继续下一个视频~')
    else:
        print('继续识别~')
            



