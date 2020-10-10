#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: xag 
@license: Apache Licence  
@contact: xinganguo@gmail.com 
@site: http://www.xingag.top 
@software: PyCharm 
@file: baidu_utils.py 
@time: 5/14/19 17:27 
@description：利用百度人脸识别API来识别人脸，获取性别、年龄、颜值等属性值
"""

import base64
import urllib
import json
import requests
import json

# 百度图像
# https://console.bce.baidu.com

appid = '22783415d'
api_key = '9l0AEw61zdSjNEPkX1WKxEVI'
secret_key = 'ZLAoRjDqdVsO8MlifVGjVK87G6LrHuAB'

# appid = '你申请的appid'
# api_key = '你申请的api_key'
# secret_key = '你申请的secret_key'

# 图片类型【网络和本地】
TYPE_IMAGE_NETWORK = 0
TYPE_IMAGE_LOCAL = 1


def get_access_token():
    """
     其关access_token有效期一般有一个月（具体看返回的json_result['"expires_in"']，单位秒），所以不用每次请求都去申请一次access_token，虽然官方容许每次都请求这种操作
    """
    client_id = api_key  # 此变量赋值成自己API Key的值
    client_secret = secret_key  # 此变量赋值成自己Secret Key的值
    auth_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}

    response_at = requests.get(auth_url, headers=header_dict)
    json_result = json.loads(response_at.text)
    access_token = json_result['access_token']
    return access_token


def identify_image(pic_url, pic_type, url_fi):
    """
    识别图片，返回识别到的人脸列表
    :param pic_url: 图片地址【网络图片或者本地图片】
    :param pic_type: 图片类型
    :param url_fi: 解析地址
    :return:
    """
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }

    if pic_type == TYPE_IMAGE_NETWORK:
        image = pic_url
        image_type = 'URL'
    else:
        with open(pic_url, 'rb') as file:
            image = base64.b64encode(file.read())
        image_type = 'BASE64'

    post_data = {
        'image': image
        # 'image': image,
        # 'image_type': image_type,
        # 'face_field': 'facetype,gender,age,beauty',  # expression,faceshape,landmark,race,quality,glasses
        # 'max_face_num': 2
    }

    response_fi = requests.post(url_fi, headers=headers, data=post_data)
    json_fi_result = json.loads(response_fi.text)
    print("getting result")

    print(json_fi_result)

    return json_fi_result["result"]


# 此函数用于解析进行人脸图片，输出图片上的人脸的性别、年龄、颜值
# 此函数调用get_access_token、identify_faces
def parse_image_pic(pic_url, pic_type, access_token):
    """
    人脸识别
    5秒之内
    :param pic_url:
    :param pic_type:
    :param access_token:
    :return:
    """
    url_fi = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token=' + access_token

    # 调用identify_faces，获取人脸列表
    json_image = identify_image(pic_url, pic_type, url_fi)

    if not json_image:
        print('未识别到物体')
        return None
    else:
        # 返回所有的人脸
        return json_image


def analysis_image(result):
    """
    分析人脸，判断颜值是否达标
    18-30之间，女，颜值大于70
    :param face_list:识别的脸的列表
    :return:
    """
    # 是否能找到旗帜
    find_flag = False
    print('一共识别到%d个物体，下面开始识别是否有旗帜~' % len(result))
    for obj in result:
        if obj["keyword"] == "旗帜":
            find_flag = True
            break

        else:
            continue

    return find_flag

