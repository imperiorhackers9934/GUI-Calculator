#Importing Tkinter and its requirements
from tkinter import *
import tkinter
root = Tk() #Initialising tkinter
root.title("My Calculator")
root.geometry("402x395")
#This list Containes the numbers and the operators on which the operation is being performed
mylist=[]
#Function that converts list elements to single string
def lts(list):
  mystr = ''.join(list)
  return mystr
#Calculates the output
def calculate():
  return (eval(lts(mylist)))
#Appends the calculated value to the list
def setValue(num):
  mylist.append(str(num))
#Updates the Entry Widget when list is changed
def update():
    e["state"] = "normal"
    e.delete(0, tkinter.END)
    e.insert(tkinter.END,lts(mylist))
    e["state"] = "readonly"
    e.after(100,update)
#Calculate the Value of the operation and appends it to list
def hello():
   value = calculate() 
   del mylist[:]
   setValue(value)
#Deletes all the elements of list
def clear():
  del mylist[:] 
#Deletes last element only
def clearlast():
   del mylist[-1]
#From here the main GUI Program Starts
e = Entry(root,font=("default", 27 ),bg="black")
e["state"] = "readonly"
e.place(x=0,y=0)
update()
Button(root,text="1",width=10,height=5,command=lambda:setValue(1)).place(x=0,y=50)
Button(root,text="2",width=10,height=5,command=lambda:setValue(2)).place(x=0,y=135)
Button(root,text="3",width=10,height=5,command=lambda:setValue(3)).place(x=0,y=220)
Button(root,text="4",width=10,height=5,command=lambda:setValue(4)).place(x=80,y=50)
Button(root,text="5",width=10,height=5,command=lambda:setValue(5)).place(x=80,y=135)
Button(root,text="6",width=10,height=5,command=lambda:setValue(6)).place(x=80,y=220)
Button(root,text="7",width=10,height=5,command=lambda:setValue(7)).place(x=160,y=50)
Button(root,text="8",width=10,height=5,command=lambda:setValue(8)).place(x=160,y=135)
Button(root,text="9",width=10,height=5,command=lambda:setValue(9)).place(x=160,y=220)
Button(root,text="+",width=10,height=5,command=lambda:setValue("+")).place(x=240,y=50)
Button(root,text="-",width=10,height=5,command=lambda:setValue("-")).place(x=240,y=135)
Button(root,text="x",width=10,height=5,command=lambda:setValue("*")).place(x=240,y=220)
Button(root,text="/",width=10,height=5,command=lambda:setValue("/")).place(x=320,y=50)
Button(root,text="<--",width=10,height=5,command=lambda:clearlast()).place(x=320,y=135)
Button(root,width=10,height=5,text="AC",command=lambda:clear()).place(x=320,y=220)
Button(root,width=32,height=5,text="=",command=lambda:hello()).place(x=4,y=306)
Button(root,width=10,height=5,text="0",command=lambda:setValue("0")).place(x=240,y=306)
Button(root,width=10,height=5,text=".",command=lambda:setValue(".")).place(x=320,y=306)
root.mainloop()
