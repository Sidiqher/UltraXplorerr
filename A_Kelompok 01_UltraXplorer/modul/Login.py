from tkinter import *
import tkinter as tk
from tkinter import messagebox
import Program as md
import os

# Menampilkan menu login dan create account
def mainprogram():
    global username_value
    font_login = "Roboto Condensed"
    
    window = tk.Tk()
    window.title("Login")
    window.geometry("1200x675")
    window.configure(bg="White")
    window.resizable(True,True)

    img = PhotoImage(file="gambar/Modern Initial E Logo.png")
    Label(window,image=img,bg="White").place(x=175,y=125)

    frame = Frame(window,width=350,height=350,bg="White")
    frame.place(x=600,y=200)

    heading = Label(frame,text="Sign in", fg="#57a1f8",bg="White",font=("Montserrat",23,"bold"))
    heading.place(x=100,y=5)

    #===========================================================================================================#
# Menyimpan account user dan password
    def sign_up():
        global username_value2
        username_value2 = username2.get()
        password_value2= password2.get()
        file1 = open("databaseuser/logindatabase.csv", "r")
        for i in file1:
            z = 0
            a,b = i.split(",")
            b = b.strip()
            if username_value2 == "" or password_value2 == "" or username_value2 == "username" or password_value2 == "password":
                messagebox.showerror("Error","Username/Password tidak boleh kosong")
                break
            elif username_value2 == a:
                messagebox.showinfo("Error", "Username sudah ada silahkan ganti username")
                break
            else:
                z = z + 1

        if z == len(i[0]):    
                file = open("databaseuser/logindatabase.csv", "a")
                file.write(f"{username_value2},{password_value2}\n")
                file.close()
                os.makedirs(f"databaseuser/{username_value2}")
                
                file = open(f"databaseuser/{username_value2}/nilai quiz.csv", "w")
                file.write("Mata Kuliah,nilai1,nilai2,nilai3,nilai4,nilai5\n")
                file.close()
                
                file = open(f"databaseuser/{username_value2}/nilai tugas.csv", "w")
                file.write("Mata Kuliah,nilai1,nilai2,nilai3,nilai4,nilai5\n")
                file.close()

                file = open(f"databaseuser/{username_value2}/nilai UTS-UAs.csv", "w")
                file.write("Mata Kuliah,nilai1,nilai2\n")
                file.close()

                messagebox.showinfo("Berhasil","Sign Up telah berhasil silahkan login ulang")
                screen.destroy()
                mainprogram()
                
        file1.close()


    def back_login():
        screen.destroy()
        mainprogram()

# Masuk ke dalam program utama
    def login():
        global username2
        global username_value
        username_value = username.get()
        password_value = password.get()
        j = 0
        c = 0

        if username_value == "username" or password_value == "password":
            messagebox.showerror("Error","Username/Password tidak boleh kosong")
        else:
            file = open("databaseuser/logindatabase.csv", "r")
            for i in file:
                c += 1
                a,b = i.split(",")
                b = b.strip()

                if (a == username_value and b == password_value):
                    window.destroy()
                    md.program()
                    break
                else:
                    j += 1

            if j == c:
                messagebox.showinfo("Error", "Akun anda tidak ditemukan")
                
            file.close()

# Menampilkan window untuk create account
    def signup():
        global username2
        global password2
        global screen
        window.destroy()
        screen=tk.Tk()
        screen.title(f"Create Account")
        screen.geometry("925x500+300+200")
        frame = Frame(screen,width=350,height=350,bg="White")
        frame.place(x=400,y=100)
        heading = Label(frame,text="Sign Up", fg="#57a1f8",bg="White",font=("Montserrat",23,"bold"))
        heading.place(x=100,y=5)
        back_button = Button(screen,width=3,text="Back",font=(font_login,11,"underline"), fg="Black",cursor="hand2",border=0,command=back_login)
        back_button.place(x=10,y=10)


        def on_enter(e):
            username2.delete(0, "end")

        def on_leave(e):
            if username2 == username2.get():
                username2.delete(0, "end")

        username2= Entry(frame,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
        username2.place(x=60,y=75)
        username2.insert(0,"username")
        username2.bind("<FocusIn>", on_enter)
        username2.bind("<FocusOut>", on_leave)

        #===========================================================================================================#
        def on_enter(e):
            password2.delete(0, "end")

        def on_leave(e):
            if password2 == password2.get():
                password2.delete(0, "end")

        password2 = Entry(frame,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
        password2.place(x=60,y=115)
        password2.insert(0,"password")
        password2.bind("<FocusIn>", on_enter)
        password2.bind("<FocusOut>", on_leave)

        #===========================================================================================================#

        Button(frame,width=29,height=1,text="Create Account", fg="white",bg="#57a1f8",border=0).place(x=60,y=185)

        signup_button = Button(frame,width=29,text="Create Account", fg="White",bg="#57a1f8",cursor="hand2",border=0,command = sign_up)
        signup_button.place(x=60,y=185)


    #===========================================================================================================#
    def on_enter(e):
        username.delete(0, "end")

    def on_leave(e):
        if username == username.get():
            username.delete(0, "end")

    username = Entry(frame,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
    username.place(x=60,y=75)
    username.insert(0,"username")
    username.bind("<FocusIn>", on_enter)
    username.bind("<FocusOut>", on_leave)
    

    #===========================================================================================================#
    def on_enter(e):
        password.delete(0, "end")

    def on_leave(e):
        if password == password.get():
            password.delete(0, "end")

    password = Entry(frame,width=25, fg = "black", border="2",bg="White",font=(font_login,11))
    password.place(x=60,y=115)
    password.insert(0,"password")
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    #===========================================================================================================#
    Button(frame,width=29,height=1,text="Login", fg="white",bg="#57a1f8",border=0).place(x=60,y=155)

    login = Button(frame,width=29,text="Login", fg="White",bg="#57a1f8",cursor="hand2",border=0,command = login)
    login.place(x=60,y=155)

    Button(frame,width=29,height=1,text="Create Account", fg="white",bg="#57a1f8",border=0).place(x=60,y=185)

    signup = Button(frame,width=29,text="Create Account", fg="White",bg="#57a1f8",cursor="hand2",border=0,command = signup)
    signup.place(x=60,y=185)

    #===========================================================================================================#


    window.mainloop()


if __name__=="__main__":
    mainprogram()
