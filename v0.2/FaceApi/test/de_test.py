import requests
from util import base64tool

base64_code = base64tool.signuptobase64()
print base64_code


api_url = "https://api-cn.faceplusplus.com/facepp/v3/detect?" \
          "api_key=dBDgK-yTfHusyI2rHtHPz8vQn3woE0KZ&" \
          "api_secret=fnxB38IaaPSzA45eEkZvc-6drk38AQzD"



data = {"image_base64":base64_code}
rep = requests.post(api_url, data=data)
result = rep.json()
print result

face_token = result['faces'][0]["face_token"]
print face_token