from tkinter import *
import tkinter as tk

def login():
    font_login = "Roboto Condensed"
    
    window = Tk()
    window.title("Login")
    window.geometry("1200x675")
    window.configure(bg="Red")
    window.resizable(True,True)


    img = PhotoImage(file="gambar/Modern Initial E Logo.png")
    Label(window,image=img, bg="White").place(x=50,y=50)

    username = Entry(window,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
    username.place(x=800,y=300)
    
    password = Entry(window,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
    password.place(x=800,y=330)

    Button(window,width=29,height=1,text="Login", fg="white",bg="#57a1f8").place(x=800,y=360)

    Button(window,width=29,height=1,text="Register", fg="white",bg="#57a1f8").place(x=800,y=390)

    window.mainloop()
if __name__=="__main__":
    login()