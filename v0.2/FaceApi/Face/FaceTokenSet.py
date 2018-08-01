import requests
import json



#class Facereg:
# def createSet():
#     api_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create?" \
#               "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
#               "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD&" \
#               "display_name = FaceRegLogin"
#
#     rep = requests.post(api_url)
#     result =  rep.json()
#     faceset_token =  result["faceset_token"]
#     return faceset_token




def addFacetoSet(FacesetToken,Face_token):
    api_url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create?' \
              'api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&' \
              'api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD&' \
              'faceset_token=' + FacesetToken + "&" \
              "face_token=" + Face_token
    rep = requests.post(api_url)
    return True



def getFaceSets():
    api_url = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets?" \
              "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
              "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD"
    rep = requests.post(api_url)
    result = rep.json()
    return result["facesets"][0]["faceset_token"]

