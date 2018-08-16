from faceRecognition.Signup import signup
from utils import utils
from faceRecognition.Login import login


utils.savesignupFile()
base64 = utils.signuptobase64()
face_token = utils.detect(base64)
print(face_token)
a = signup(face_token)
a.signup()

utils.saveloginFile()
base64 = utils.logintobase64()
face_token = utils.detect(base64)
print(face_token)
b = login(face_token,a.getFaceSet())
b.login()
