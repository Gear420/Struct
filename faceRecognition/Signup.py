import requests
from utils import utils

class signup(object):
    def __init__(self,face_token):
        self.face_token = face_token


     def getFaceSet(self):
        api_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets?" \
              "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
              "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD"
        rep = requests.post(api_url)
        result = rep.json()

        print result["facesets"][0]["faceset_token"]
        return result["facesets"][0]["faceset_token"]

    def addFacetoSet(self,FacesetToken, Face_token):
        api_url = ' https://api-cn.faceplusplus.com/facepp/v3/faceset/addface?' \
                  'api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&' \
                  'api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD&' \
                  'faceset_token=' + FacesetToken + "&" \
                  "face_tokens=" + Face_token
        rep = requests.post(api_url)
        result = rep.json()
        print result

    def signup(self):
        self.addFacetoSet(self.getFaceSet(),self.face_token)



