#coding=utf-8
from tkinter import *
import cv2
from util.saveFilebyOpencv import *
from util import saveFilebyOpencv
from util import base64tool
from Face import FaceReg
from Face import Faceauth
from Face import FaceTokenSet



import pykinect2



class Reg(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (270, 480))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.login = Frame(self.root,width =270 ,height = 120,bg = "green")
        self.choose = Frame(self.root,width = 270,height = 360)

        self.login.grid(row = 0,column = 0)
        self.choose.grid(row=1,column = 0,pady = 100)


        self.blank  = Label(self.login,text = "              ")
        self.blank2 = Label()
        self.welcome = Label(self.login,text = "这里是欢迎信息")
        self.loginbutton = Button(self.login,text = "登录",command = self.Submit)
        self.sighupbutton = Button(self.login,text = "注册",command = self.SignUp)


        self.welcome.grid(row = 0,column= 0)
        self.blank.grid(row = 0,column =1)
        self.loginbutton.grid(row = 0, column =2)
        self.sighupbutton.grid(row = 0,column =3)


        self.bodyreg = Button(self.choose,text = '体能评估',command = self.Bodyreg)
        self.sportguide = Button(self.choose,text = "运动指导")
        self.titaijiance = Button(self.choose,text = "体态监测")
        self.meiyan = Button(self.choose,text ="智动美颜")


        self.bodyreg.grid(row = 1,column = 0 , padx = 40)
        self.titaijiance.grid(row = 2, column = 0)
        self.meiyan.grid(row = 2,column =1 ,pady =100)
        self.sportguide.grid(row = 1, column = 1)

        #self.loginbutton.pack(side = RIGHT)

        #self.button = Button(self.frame,text = "登录",command = self.Submit)
        #self.button.pack()



        #self.lab3 = Label(self.frame,text = "")
        #self.lab3.pack()


        #self.button2 = Button(self.frame,text = "退出",command = self.frame.quit)
        #self.button2.pack()

        #self.button3 = Button(self.frame,text = '注册',command = self.SignUp)
        #self.button3.pack()


    def Bodyreg(self):
        self.choose.destroy()




    def Submit(self):

        #saveloginFile()
        #base64 = base64tool.logintobase64()
        #facetoken = FaceReg.detect(base64)
        #if Faceauth.auth(self.FacesetToken,facetoken):
        #self.lab3["text"] = "人脸认证成功"
        #else:
        #self.lab3["text"] = "人脸认证失败"
        #TODO功能选择界面
        self.login.destroy()







    def SignUp(self):
        #savesignupFile()
        #base64 = base64tool.signuptobase64()
        #facetoken = FaceReg.detect(base64)
        #if FaceTokenSet.addFacetoSet(self.FacesetToken,facetoken):
        self.lab3["text"] = "注册成功"
        #self.Submit()


    def StaticReg(self):
        pass




root = Tk()
root.title("登录界面")
app = Reg(root)

root.mainloop()

