#coding=utf-8
from tkinter import *
from util.saveFilebyOpencv import *
from util import saveFilebyOpencv
from util import base64tool
from Face import FaceReg
from Face import Faceauth
from Face import FaceTokenSet









class Reg(Frame):
    def __init__(self,master,FacesetToken):

        self.FacesetToken = FacesetToken


        frame = Frame(master)
        frame.pack()

        self.button = Button(frame,text = "登录",command = self.Submit)
        self.button.grid(row = 2,column = 1,sticky = E)
        self.lab3 = Label(frame,text = "")
        self.lab3.grid(row = 3,column = 0,sticky = W)


        self.button2 = Button(frame,text = "退出",command = frame.quit)
        self.button2.grid(row = 3,column = 3,sticky = E)



        self.button3 = Button(frame,text = '注册',command = self.SignUp)
        self.button3.grid(row=2, column=2, sticky=E)




    def Submit(self):
        saveloginFile()
        base64 = base64tool.logintobase64()
        facetoken = FaceReg.detect(base64)
        if Faceauth.auth(self.FacesetToken,facetoken):
            self.lab3["text"] = "人脸认证成功"
        else:
            self.lab3["text"] = "人脸认证失败"
        #TODO功能选择界面




    def SignUp(self):
        savesignupFile()
        base64 = base64tool.signuptobase64()
        facetoken = FaceReg.detect(base64)
        if FaceTokenSet.addFacetoSet(self.FacesetToken,facetoken):
            self.lab3["text"] = "注册成功"
        self.Submit()



