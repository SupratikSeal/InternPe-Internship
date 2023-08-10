from tkinter import *
import time

#time function code
def clock():
    t=time.strftime("%H:%M:%S %p")
    x.config(text=t)
    x.after(1000,clock)  #update the funtion after 1000ms (calling it again)
    
#GUI code
root=Tk()
root.title("Digital Clock")
root.geometry("300x60")
x=Label(root,font="Arial 50",fg="white",bg='grey')
x.pack()

clock() #calling time function
root.mainloop() 