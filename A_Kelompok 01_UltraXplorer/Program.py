from tkinter import *
import tkinter as tk
from tkinter import messagebox
import modul.Login 
import csv
import modul.idcard
import modul.tabel as tbl
import modul.grafik as gr
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modul.send_email import send_png_email
import smtplib

font_main = "Roboto Condensed"

def program():
    global username_user
    global window2
    global a    
    global n
    a = 0
    n = 0
    username_user = modul.Login.username_value
    window2 = tk.Tk()
    window2.title(f"UltraXplorer {modul.Login.username_value}")
    window2.geometry("1200x675")
    
    img = PhotoImage(file="gambar/bg1.png")
    Label(window2,image=img,bg="White").place(x=248,y=0)
    window2.resizable(False,False)

    frame = Frame(window2,width=250,height=675,bg="#403F64", border = "1")
    frame.place(x=0,y=0)

# Menghapus progres sebelumnya dan masuk ke menu manajemen akun
    def manajemen_akun0():
        if a == 1:
            frame2.destroy()

        if n == 1:
            gambar.destroy()
            cetak.destroy()      
        manajemen_akun()

# Menampilkan menu manajemen akun 
    def manajemen_akun():
        global ganti_biodata
        global frame2
        global a
        frame2 = Frame(window2,width=800,height=400,bg="#F8B410")
        frame2.place(x=350,y=100)

        def simpan_biodata():
            file_biodata = open(f"databaseuser/{username_user}/biodata.csv", "w")
            text_biodata = f"""Nama,NIM,Email
{nama.get()},{nim.get()},{tgllahir.get()}"""
            file_biodata.write(text_biodata)
            file_biodata.close()
            messagebox.showinfo("Berhasil","Data Biodata Telah Disimpan")
            manajemen_akun0()

        def change_biodata():
            global nama
            global nim 
            global tgllahir
            ganti_biodata = Button(frame2,width=28,pady=3,text="Simpan Biodata",font=(font_main,11),fg="White",bg="black",cursor="hand2",border=0,command=simpan_biodata)
            ganti_biodata.place(x=100,y=260)       

            nama = Entry(frame2,width=40, fg = "black", border="1",bg="White",font=(font_main,15))
            nama.place(x=208,y=120)

            nim = Entry(frame2,width=40, fg = "black", border="1",bg="White",font=(font_main,15))
            nim.place(x=208,y=155)

            tgllahir = Entry(frame2,width=40, fg = "black", border="1",bg="White",font=(font_main,15))
            tgllahir.place(x=208,y=190)

            text_biodata = f"""
Nama\t\t :

NIM \t\t :

Email\t\t :
                """

            biodata = Label(frame2,text=text_biodata,justify="left",fg="black",bg="#F8B410",font=(font_main,12))
            biodata.place(x=50,y=100)
       
        try:
            with open(f"databaseuser/{username_user}/biodata.csv") as data_biodata:
                data = csv.reader(data_biodata,delimiter=",")
                data = list(data)

                text_biodata = f"""
Nama\t\t : {data[1][0]}

NIM\t\t : {data[1][1]}

Email\t\t : {data[1][2]}
                """

                biodata = Label(frame2,text=text_biodata,justify="left",fg="black",bg="#F8B410",font=(font_main,12))
                biodata.place(x=50,y=100)

                ganti_biodata = Button(frame2,width=28,pady=3,text="Edit Biodata",font=(font_main,11),fg="White",bg="black",cursor="hand2",border=0,command=change_biodata)
                ganti_biodata.place(x=100,y=260)

        except FileNotFoundError or PermissionError or UnboundLocalError:
            text_biodata = f"""
Nama\t\t :

NIM\t\t :

Email\t :
                """

            biodata = Label(frame2,text=text_biodata,justify="left",fg="black",bg="#F8B410",font=(font_main,12))
            biodata.place(x=50,y=100)

            ganti_biodata = Button(frame2,width=28,pady=3,text="Edit Biodata",font=(font_main,11),fg="White",bg="black",cursor="hand2",border=0,command=change_biodata)
            ganti_biodata.place(x=100,y=260)
        
        a = 1

# Menampilkan menu beranda
    def beranda0():
        if a == 1:
            frame2.destroy()

        if n == 1:
            gambar.destroy()
            cetak.destroy() 

        beranda()

    def beranda():
        global frame2
        global a
        frame2 = Frame(window2,width=800,height=400,bg="#F8B410")
        frame2.place(x=350,y=100)

        text = """
-------Halo Selamat Datang di UltraXplorer------

UltraXplorer merupakan program yang dirancang untuk 
memantau perkembangan nilai yang telah diinput oleh user
UltraXplorer dapat menampilkan grafik perkembangan 
dan mencetak id card   
        
        
        """
        heading = Label(frame2,text= text, fg="black",font=(font_main,15,"bold"), justify="left", background= "#F8B410")
        heading.place(x=60,y=100)

        a = 1                

# Menghapus progres sebelumnya dan masuk ke menu tambah matkul
    def tambahmatkul0():
        if a == 1:
            frame2.destroy()        
        if n == 1:
            gambar.destroy()
            cetak.destroy()
        tambahmatkul()

# Menampilkan menu tambah matkul
    def tambahmatkul():
        global frame2
        global a
        def simpan_matkul():
            matkul_value = input_matkul.get()
            v = 0
            w = 0
            if matkul_value == "":
                messagebox.showerror("error","nama matkul tidak boleh kosong")
                v = 1
                tambahmatkul0()
            else:
                with open(f"databaseuser/{username_user}/nilai quiz.csv") as matkul:
                    matkul = csv.reader(matkul,delimiter=",")
                    matkul = list(matkul)
                    for i in matkul:
                        w +=1
                        if i[0].lower() == matkul_value.lower():
                            messagebox.showinfo("error","Nama mata kuliah sudah ada")
                            tambahmatkul0()
                            break
                        else:
                            v += 1
            if v == w:
                file_nilai = open(f"databaseuser/{username_user}/nilai quiz.csv","a")
                file_nilai.write(f"{matkul_value}\n")
                file_nilai.close()

                file_nilai = open(f"databaseuser/{username_user}/nilai tugas.csv","a")
                file_nilai.write(f"{matkul_value}\n")
                file_nilai.close()

                file_nilai = open(f"databaseuser/{username_user}/nilai UTS-UAS.csv","a")
                file_nilai.write(f"{matkul_value}\n")
                file_nilai.close()

                messagebox.showinfo("Berhasil","Mata kuliah telah ditambahkan")
                tambahmatkul0()

        a = 1

        frame2 = Frame(window2,width=630,height=250,bg="#F8B410")
        frame2.place(x=400,y=200)

        label_matkul = Label(frame2,text="Masukkan Mata Kuliah Baru:", fg="black",bg="#F8B410",font=(font_main,15,"bold"))
        label_matkul.place(x=40,y=80)

        input_matkul = Entry(frame2,width=40, fg = "black", border="1",bg="White",font=(font_main,15))
        input_matkul.place(x=40,y=120)

        inputmatkulbutton = Button(frame2,width=40,pady=3,text="Tambah Mata Kuliah",font=(font_main,11),fg="White",bg="#403F64",cursor="hand2",border=0,command=simpan_matkul)
        inputmatkulbutton.place(x=40,y=160)

# Menghapus progres sebelumnya dan masuk ke menu cek nilai
    def ceknilai0():
        if a == 1:
            frame2.destroy()                
        if n == 1:
            gambar.destroy()
            cetak.destroy()
        ceknilai()

# Masuk ke menu cek nilai
    def ceknilai():
        global frame2
        global a

        frame2 = Frame(window2,width=950,height=575,bg="#F8B511")
        frame2.place(x=250,y=50)

        def tabel1(n):
            global f
            global frame2
            file = open(f"databaseuser/{username_user}/nilai quiz.csv")
            file = csv.reader(file,delimiter=",")
            file = list(file)
            f = -1
            for i in range(len(file)):
                f += 1
                if n[0][0]== file[i][0]:
                    break
            matkul.destroy()
            frame2.destroy()
            frame2 = Frame(window2,width=950,height=575,bg="#F8B511")
            frame2.place(x=250,y=50)
            button1 = Button(frame2,width=10,text="Nilai Quiz",fg="black",bg="#F8B511",font=(font_main,12),border=0,command=nilaiquiz)
            button1.place(x=300,y=550)
            button2 = Button(frame2,width=11,text="Nilai Tugas",fg="black",bg="#F8B511",font=(font_main,12),border=0,command=nilaitugas)
            button2.place(x=390,y=550)                
            button3 = Button(frame2,width=12,text="Nilai UTS/UAS",fg="black",bg="#F8B511",font=(font_main,12),border=0,command=nilai_uts_uas)
            button3.place(x=500,y=550)
            nilaiquiz()

        def nilaiquiz():
            heading = Label(frame2,text="Nilai Quiz", fg="Black", bg = "#F8B511",padx=30, font=(font_main,12,"bold"))
            heading.place(x=10,y=5)
            with open(f"databaseuser/{username_user}/nilai quiz.csv") as data:
                data = csv.reader(data, delimiter=",")
                data = list(data)
            data2 = data[f]
            datalist = []
            datalist.append(data2)
            gr.grafik(datalist)
            tbl.tabel(datalist)
                         
            canvas = FigureCanvasTkAgg(gr.fig,master=frame2)
            canvas.draw()
            canvas.get_tk_widget().place(x=20,y=50)
                
            output_text = tk.Text(frame2, width=120,bg="#F8B511", height=5,border=0)
            output_text.insert(tk.END, tbl.table)
            output_text.place(x=20,y=350)

            def tambahnilai():
                    try:
                        simpannilai_value = float(simpannilai.get())
                        with open(f"databaseuser/{username_user}/nilai quiz.csv","r") as nilai:
                            nilai = csv.reader(nilai)
                            nilai = list(nilai)
                        nilai_baru = nilai[f]
                        if len(nilai_baru) == 6:
                            messagebox.showinfo("Error","Maaf, saat ini program hanya dapat menginputkan 5 nilai")
                        else:
                            nilai_baru.append(simpannilai_value)
                            with open(f"databaseuser/{username_user}/nilai quiz.csv", 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(nilai)
                            messagebox.showinfo("Berhasil","Nilai berhasil ditambahkan")
                    except ValueError:
                        messagebox.showerror("Gagal", "Nilai tidak berhasil ditambahkan")
                    
            simpannilai = Entry(frame2,width=20,fg="black",bg="white",font=(font_main,10),border=0)
            simpannilai.place(x=70,y=480)

            tambah_nilai = Button(frame2,width=20,text="Tambah Nilai",fg="black",bg="white",font=(font_main,12),border=0,command=tambahnilai)
            tambah_nilai.place(x=70,y=510)

        def nilaitugas():
            global frame2
            heading = Label(frame2,text="Nilai Tugas", fg="Black", bg = "#F8B511",padx=30, font=(font_main,12,"bold"))
            heading.place(x=10,y=5)
            with open(f"databaseuser/{username_user}/nilai tugas.csv") as data:
                data = csv.reader(data, delimiter=",")
                data = list(data)
                data = data[f]
                datalist = []
                datalist.append(data)
                gr.grafik(datalist)
                tbl.tabel(datalist)
                    
                canvas = FigureCanvasTkAgg(gr.fig,master=frame2)
                canvas.draw()
                canvas.get_tk_widget().place(x=20,y=50)

                output_text = tk.Text(frame2, width=120,bg="#F8B511", height=5,border=0)
                output_text.insert(tk.END, tbl.table)
                output_text.place(x=20,y=350)


            def tambahnilai():
                    try:
                        simpannilai_value = float(simpannilai.get())
                        with open(f"databaseuser/{username_user}/nilai tugas.csv","r") as nilai:
                            nilai = csv.reader(nilai)
                            nilai = list(nilai)
                        nilai_baru = nilai[f]
                        if len(nilai_baru) == 6:
                            messagebox.showinfo("Error","Maaf, saat ini program hanya dapat menginputkan 5 nilai")
                        else:
                            nilai_baru.append(simpannilai_value)
                            with open(f"databaseuser/{username_user}/nilai tugas.csv", 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(nilai)
                            messagebox.showinfo("Berhasil","Nilai berhasil ditambahkan")
                    except ValueError:
                        messagebox.showerror("Gagal", "Nilai tidak berhasil ditambahkan")

            simpannilai = Entry(frame2,width=20,fg="black",bg="white",font=(font_main,10),border=0)
            simpannilai.place(x=70,y=480)
                
            tambah_nilai = Button(frame2,width=20,text="Tambah Nilai",fg="black",bg="white",font=(font_main,12),border=0,command=tambahnilai)
            tambah_nilai.place(x=70,y=510)
                
        def nilai_uts_uas():
            global frame2
            heading = Label(frame2,text="Nilai UTS-UAS", fg="Black", bg = "#F8B511",padx=10, font=(font_main,12,"bold"))
            heading.place(x=10,y=5)
            global n
            with open(f"databaseuser/{username_user}/nilai UTS-UAS.csv") as data:
                data = csv.reader(data, delimiter=",")
                data = list(data)
                data = data[f]
                datalist = []
                datalist.append(data)
                gr.grafik(datalist)
                tbl.tabel2(datalist)
                        
                canvas = FigureCanvasTkAgg(gr.fig,master=frame2)
                canvas.draw()
                canvas.get_tk_widget().place(x=20,y=50)

                output_text = tk.Text(frame2, width=120,bg="#F8B511", height=5,border=0)
                output_text.insert(tk.END, tbl.table)
                output_text.place(x=20,y=350)

            def tambahnilai():
                    try:
                        simpannilai_value = float(simpannilai.get())
                        with open(f"databaseuser/{username_user}/nilai UTS-UAS.csv","r") as nilai:
                            nilai = csv.reader(nilai)
                            nilai = list(nilai)
                        nilai_baru = nilai[f]
                        if len(nilai_baru) == 3:
                            messagebox.showinfo("Error","Maaf, saat ini program hanya dapat menginputkan 2 nilai")
                        else:
                            nilai_baru.append(simpannilai_value)
                            with open(f"databaseuser/{username_user}/nilai UTS-UAS.csv", 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerows(nilai)
                            messagebox.showinfo("Berhasil","Nilai berhasil ditambahkan")
                    except ValueError:
                        messagebox.showerror("Gagal", "Nilai tidak berhasil ditambahkan")
                
            simpannilai = Entry(frame2,width=20,fg="black",bg="white",font=(font_main,10),border=0)
            simpannilai.place(x=70,y=480)
            tambah_nilai = Button(frame2,width=20,text="Tambah Nilai",fg="black",bg="white",font=(font_main,12),border=0,command=tambahnilai)
            tambah_nilai.place(x=70,y=510)

        def hapus_matkul(n):
            global f
            global frame2
            file = open(f"databaseuser/{username_user}/nilai quiz.csv")
            file = csv.reader(file,delimiter=",")
            file = list(file)
            f = -1
            for i in range(len(file)):
                f += 1
                if n[0][0]== file[i][0]:
                    break

            with open(f"databaseuser/{username_user}/nilai quiz.csv") as data_nilai:
                data_nilai = csv.reader(data_nilai)
                data_nilai = list(data_nilai)
                data_nilai.pop(f)
            with open(f"databaseuser/{username_user}/nilai quiz.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_nilai)
            with open(f"databaseuser/{username_user}/nilai tugas.csv") as data_nilai:
                data_nilai = csv.reader(data_nilai)
                data_nilai = list(data_nilai)
                data_nilai.pop(f)
            with open(f"databaseuser/{username_user}/nilai tugas.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_nilai)
            with open(f"databaseuser/{username_user}/nilai UTS-UAS.csv") as data_nilai:
                data_nilai = csv.reader(data_nilai)
                data_nilai = list(data_nilai)
                data_nilai.pop(f)
            with open(f"databaseuser/{username_user}/nilai UTS-UAS.csv", 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data_nilai)
            messagebox.showinfo("Berhasil", f"Mata kuliah berhasil dihapus")
            ceknilai0()
                

        with open(f"databaseuser/{username_user}/nilai quiz.csv") as nilai:
            nilai = csv.reader(nilai,delimiter=",")
            nilai = list(nilai)                
            letak = 50
            n = 0
            for i in nilai[1:]:
                n += 1
                matkul =  Button(frame2,text=i[0],width=50,justify="left",fg="white",bg="#403F64",font=(font_main,12),border=0,command=lambda n=nilai[n:n+1]: tabel1(n))
                matkul.place(x=50,y=letak)
                hapus =  Button(frame2,text="X",width=3,justify="left",fg="white",bg="red",font=(font_main,12),border=0,command=lambda n=nilai[n:n+1]: hapus_matkul(n))
                hapus.place(x=520,y=letak)
                letak += 50    
                
        if letak == 50:
            Label(frame2,width=50,justify="left",text="silahkan tambah mata kuliah terlebih dahulu",fg="white",bg="#403F64",font=(font_main,12),border=0).place(x=50,y=50)

        a = 1

# Menghapus progres sebelumnya dan masuk ke menu cetak id card
    def cetakcard0():  
        if a == 1:
            frame2.destroy()                
        if n == 1:
            gambar.destroy()
            cetak.destroy()
        cetakcard()

# Masuk ke menu cetak id card
    def cetakcard():
        global n
        global gambar
        global frame2
        global cetak
        j = 0
        frame2 = Frame(window2,width=0,height=0,bg="yellow")
        frame2.place(x=250,y=0)

        def kirim_idcard():
            filee = open(f"databaseuser/{username_user}/biodata.csv")
            file = csv.reader(filee,delimiter=",")
            file = list(file)
            email = file[1][2]
            filee.close()
            try:
                send_png_email(email,f"databaseuser/{username_user}/idcard.png")
            except smtplib.SMTPRecipientsRefused:
                messagebox.showerror("Error","Saat ini program hanya dapat mengirim email dengan platform gmail")


        try:
            global n           
            with open(f"databaseuser/{username_user}/biodata.csv") as data_biodata:
                    data = csv.reader(data_biodata,delimiter=",")
                    data = list(data)

                    modul.idcard.buat_id_card(f"{data[1][0]}",f"{data[1][1]}",f"gambar/background_id.png",f"databaseuser/{username_user}/idcard.png")
                    
                    modul.idcard.tampilkan()
                    gambar = Label(window2,image=modul.idcard.photo,width=360,height=540)
                    gambar.place(x=545,y=30)

                    cetak = Button(window2,width=28,pady=3,text="Cetak ID Card",font=(font_main,11),fg="White",bg="#57a1f8",cursor="hand2",border=0,command=kirim_idcard)
                    cetak.place(x=600,y=600)
            n = 1 

        except FileNotFoundError:
            messagebox.showinfo("error", "Silahkan mengisi biodata terlebih dahulu")
            manajemen_akun0()

# Masuk ke menu log out account
    def logout():
        if window2.winfo_exists():
            window2.destroy()
            modul.Login.mainprogram()

# Menampilkan button pada menu akun
    akun = Button(frame,width=28,pady=4,text=username_user,font=(font_main,11),fg="White",bg="black",cursor="hand2",border=0,command=manajemen_akun0)
    akun.place(x=0,y=15)

# Menampilkan button pada menu beranda button
    berandabutton = Button(frame,width=28,pady=4,text="Beranda",font=(font_main,11),fg="Black",bg="#F8B50E",cursor="hand2",border=0,command=beranda0)
    berandabutton.place(x=0,y=55)

# Menampilkan button pada menu tambah matkul
    tambah_matkul = Button(frame,width=28,pady=4,text="Tambah Matkul",font=(font_main,11),fg="Black",bg="#F8B50E",cursor="hand2",border=0,command=tambahmatkul0)
    tambah_matkul.place(x=0,y=95)

# Menampilkan button pada menu cek nilai  
    cek_nilai = Button(frame,width=28,pady=4,text="Cek Nilai",font=(font_main,11),fg="Black",bg="#F8B50E",cursor="hand2",border=0,command=ceknilai0)
    cek_nilai.place(x=0,y=135)

# Menampilkan button pada menu cetak id card
    cetak_card = Button(frame,width=28,pady=4,text="Cetak ID Card",font=(font_main,11),fg="Black",bg="#F8B50E",cursor="hand2",border=0,command=cetakcard0)
    cetak_card.place(x=0,y=175)

# Menampilkan button pada menu log out
    log_out = Button(frame,width=28,pady=4,text="Log Out",font=(font_main,11),fg="Black",bg="#F8B50E",cursor="hand2",border=0,command=logout)
    log_out.place(x=0,y=215)


    window2.mainloop()

if __name__=="__main__":
    # program()
    modul.Login.mainprogram()

