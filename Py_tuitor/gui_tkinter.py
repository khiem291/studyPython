'''
Created on Oct 22, 2014

@author: khiemtd
'''
#===============================================================================
# import Tkinter 
# import tkMessageBox 
#  
# top = Tkinter.Tk() 
#  
# def helloCallBack(): 
#    tkMessageBox.showinfo( "Hello Python", "Hello World") 
#  
# B = Tkinter.Button(top, text ="Hello", command = helloCallBack) 
#  
# B.pack() 
# top.mainloop() 
#===============================================================================

#===============================================================================
# import Tkinter 
# import tkMessageBox 
#  
# top = Tkinter.Tk() 
#  
# C = Tkinter.Canvas(top, bg="blue", height=250, width=300) 
#  
# coord = 10, 50, 240, 210 
# arc = C.create_arc(coord, start=0, extent=150, fill="red") 
#  
# C.pack() 
# top.mainloop() 
#===============================================================================

#===============================================================================
# from Tkinter import * 
# import tkMessageBox 
# import Tkinter 
#  
# top = Tkinter.Tk() 
# CheckVar1 = IntVar() 
# CheckVar2 = IntVar() 
# C1 = Checkbutton(top, text = "Music", variable = CheckVar1,  
#                  onvalue = 1, offvalue = 0, height=5, 
#                  width = 20) 
# C2 = Checkbutton(top, text = "Video", variable = CheckVar2, 
#                  onvalue = 1, offvalue = 0, height=5,  
#                  width = 20) 
# C1.pack() 
# C2.pack() 
# top.mainloop() 
#===============================================================================

from Tkinter import * 
 
top = Tk() 
L1 = Label(top, text="User Name") 
L1.pack( side = LEFT) 
E1 = Entry(top, bd =3) 
 
E1.pack(side = RIGHT) 
 
top.mainloop() 