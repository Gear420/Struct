#coding=utf-8


import base64

def signuptobase64():
    f = open(r'Uploads/signup.jpeg', 'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    return ls_f
def logintobase64():
    f = open(r'Uploads/login.jpeg', 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    return ls_f