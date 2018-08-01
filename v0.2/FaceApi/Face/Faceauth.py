import requests
import json
from FaceReg import compare
def auth(faceset_token,face_token):
    api_url ="https://api-cn.faceplusplus.com/facepp/v3/detect?" \
            "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
            "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD&" \
            "face_token="+ face_token + "&" \
            "faceset_token=" + faceset_token

    rep = requests.post(api_url)
    result = rep.json()
    print result
    if result["results"][0]["confidence"] > 80:
        return True

    return False


