#coding=utf-8

import base64
import requests
import cv2
import pygame


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

def scale(image,position):
    point_x, point_y = pygame.mouse.get_pos()
    #print(point_x)
    #print(point_y)
    x, y = position
    w, h = image.get_size()
    #print(w)
    #print(h)

    in_x = x - w / 2 < point_x < x + w / 2
    in_y = y - h / 2 < point_y < y + h / 2
    if in_x and in_y:
        print("hello")
        image = pygame.transform.rotozoom(image, 0.0, 1.5 )
        return image
    else:
        return image
def choose(image,position):
    point_x, point_y = pygame.mouse.get_pos()
    #print(point_x)
    #print(point_y)
    x, y = position
    w, h = image.get_size()
    #print(w)
    #print(h)

    in_x = x - w / 2 < point_x < x + w / 2
    in_y = y - h / 2 < point_y < y + h / 2
    if in_x and in_y:
        array = pygame.mouse.get_pressed()
        if array[0] == 1:
            return True
        else:
            return False
    return False
