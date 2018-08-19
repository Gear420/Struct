#coding=utf-8

import requests
from faceRecognition.Signup import signup
from utils.utils import detect,logintobase64

class login(object):
    def __init__(self, face_token, faceset_token):
        face_token = detect(logintobase64())
        faceset_token = signup().getFaceSet()
        self.face_token = face_token
        self.faceset_token = faceset_token
        self.api_url = "https://api-cn.faceplusplus.com/facepp/v3/search?" \
              "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
              "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD&" \
              "face_token="+self.face_token+"&" \
              "faceset_token=" + self.faceset_token
    def login(self):
        rep = requests.post(self.api_url)
        result = rep.json()
        print "置信度:"
        con = result["results"][0]["confidence"]
        if con > 80:
            return True
        else:
            return False


