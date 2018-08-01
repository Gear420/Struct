#coding=utf-8
from Face import FaceTokenSet
from GUI.loginGUI import Reg
from tkinter import *




FaceSetToken = "95e828752dfe156684904133a9f39ec9"

print FaceSetToken




root = Tk()
root.title("登录界面")
app = Reg(root,FaceSetToken)
root.mainloop()













