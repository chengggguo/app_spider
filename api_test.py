#!/usr/bin/env python  
# encoding: utf-8  


from utils.baidu_utils import *
import time
from datetime import datetime
import shutil


print("testing")



if __name__ == '__main__':

    access_token = get_access_token()
    print("in the loop")



            # 旗帜识别
    recognite_result = analysis_image(parse_image_pic("testImage1.jpg", TYPE_IMAGE_LOCAL, access_token))




            # 含有旗帜
    if recognite_result:

        print('识别到视频含有旗帜，继续下一个视频~')
    else:
        print('继续识别~')
            



