#coding=utf-8

import base64
import requests
import cv2


def signuptobase64():
    f = open(r'../Images/signup.jpg', 'rb') #二进制方式打开图文件
    ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
    return ls_f
def logintobase64():
    f = open(r'../Images/login.jpg', 'rb')  # 二进制方式打开图文件
    ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
    return ls_f

def detect(base64_code):
    api_url ="https://api-cn.faceplusplus.com/facepp/v3/detect?" \
            "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
            "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD"

    data = {"image_base64": base64_code}
    rep = requests.post(api_url,data=data)
    result = rep.json()
    face_token =  result['faces'][0]["face_token"]
    return face_token

def saveloginFile():
    cap = cv2.VideoCapture(0)
    while (1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("../Images/login.jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()
def savesignupFile():
    cap = cv2.VideoCapture(0)
    while (1):
        # get a frame
        ret, frame = cap.read()
        # show a frame
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("../Images/signup.jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()