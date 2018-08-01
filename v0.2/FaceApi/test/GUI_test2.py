#coding=UTF-8



from tkinter import *
import time

from tkinter import *
import time

t = Tk()
t.title('与python聊天中')

# 创建frame容器
frmLT = Frame(width=500, height=320, bg='white')
frmLC = Frame(width=500, height=150, bg='red')
frmLB = Frame(width=500, height=30,  bg='')
frmRT = Frame(width=200, height=500)

frmLT.grid(row=0, column=0)
frmLC.grid(row=1, column=0)
frmLB.grid(row=2, column=0)
frmRT.grid(row=0, column=1, rowspan=3)


frmLT.grid_propagate(0)
frmLC.grid_propagate(0)
frmLB.grid_propagate(0)
frmRT.grid_propagate(0)

t.mainloop()