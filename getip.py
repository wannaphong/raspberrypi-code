"""
Get ip by gui
"""

import tkinter as tk
import socket
import tkinter.font

win=tk.Tk()
win.title("Your IP")
myFont=tkinter.font.Font(family='Helvetica',size=12,weight='bold')
def getip():
	lbutton["text"]=str((([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]) # from https://stackoverflow.com/a/1267524/11952699

def exitPro():
	win.quit()

lbutton=tk.Button(win, text='IP', width=25,height=1, command=getip) #tk.Button(win,'IP',command=getip,bg='bisque2')#,height=1,width=24)
lbutton.grid(row=0,sticky=tk.NSEW)
lbutton.pack()

exitb=tk.Button(win, text='Exit',height=1, width=6, command=exitPro)#tk.Button(win,'Exit',font=myFont,command=exitPro,bg='cyan')#,height=1,width=6)
#exitb.grid(row=1,sticky=tk.E)
exitb.pack()

tk.mainloop()
