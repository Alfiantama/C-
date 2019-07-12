from tkinter import*
from tkinter import messagebox

def persyaratan():
    top = Toplevel()

    header = Frame(top, bg = "red", height = 30)
    header.pack(side = TOP, fill = X)

    header = Frame(top, bg = "blue", height = 30)
    header.pack(side = BOTTOM, fill = X)
    
    top.title("Auto rental Car")
    top.geometry("300x200")
    label = Label(top, text ="Syarat Untuk Menyewa")
    label.pack()

    L1 = Label(top, text ="1.Memiliki SIM(Surat Izin Mengemudi)")
    L1.pack(side = LEFT)
    L1.place(x = 10, y = 60)

    
    L2 = Label(top, text ="2.Memiliki KTP(Kartu Tanda Penduduk)")
    L2.pack(side = LEFT)
    L2.place(x = 10, y = 80)

    L3 = Label(top, text ="3.Bisa mengemudikan kendaraan")
    L3.pack(side = LEFT)
    L3.place(x = 10, y = 100)

    L3 = Label(top, text ="4.Saat pengembalian harus penyewa asli")
    L3.pack(side = LEFT)
    L3.place(x = 10, y = 120)    

    button = Button(top ,text ="Kembali",command = menu)
    button.pack()
    button.place(x = 120, y = 140)
    

def pilih_mobil():
    top = Toplevel()

    header = Frame(top, bg = "red", height = 30)
    header.pack(side = TOP, fill = X)

    header = Frame(top, bg = "blue", height = 30)
    header.pack(side = BOTTOM, fill = X)
    
    top.title("Auto rental Car")
    top.geometry("350x300")
    label = Label(top, text ="Daftar Mobil Yang Tersedia")
    label.pack()

    L9 = Label(top, text ="1.Jazz       = Rp 300.000,00")
    L9.pack(side = LEFT)
    L9.place(x = 10, y = 60)
               
    L10 = Label(top, text ="2.BMW    = Rp 600.000,00")
    L10.pack(side = LEFT)
    L10.place(x = 10, y = 90)

    L11 = Label(top, text ="3.Innova  = Rp 400.000,00")
    L11.pack(side = LEFT)
    L11.place(x = 10, y = 120)

    L12 = Label(top, text="4.Pajero  = Rp 700.000,00")
    L12.pack(side = LEFT)
    L12.place(x = 10, y = 150)

    L12 = Label(top, text="5.Innova  = Rp 100.000,00")
    L12.pack(side = LEFT)
    L12.place(x = 10, y = 180)

    button4 = Button(top, text ="Lanjut", command = data_diri)
    button4.pack()
    button4.place(x = 10, y = 210)

    

def data_diri():
    
    top = Toplevel()

    header = Frame(top, bg = "red", height = 30)
    header.pack(side = TOP, fill = X)

    header = Frame(top, bg = "blue", height = 30)
    header.pack(side = BOTTOM, fill = X)
    
    top.title("Auto Rental Car")
    top.geometry("350x300")
    label = Label(top, text ="Masukan Data Diri Anda")
    label.pack()
    
    L1 = Label(top, text = "Nama Lengkap")
    L1.pack(side = LEFT)
    L1.place(x = 10, y = 50)
    E1 = Entry(top, bd = 5)
    E1.pack(side = RIGHT)
    E1.place(x = 150, y = 50)

    L2 = Label(top, text = "Alamat Peminjam")
    L2.pack(side = LEFT)
    L2.place(x = 10, y = 80)
    E2 = Entry(top, bd = 5)
    E2.pack(side = RIGHT)
    E2.place(x = 150, y = 80)

    L3 = Label(top, text = "No Telp/Hp")
    L3.pack(side = LEFT)
    L3.place(x = 10, y = 110)
    E3 = Entry(top, bd = 5)
    E3.pack(side = RIGHT)
    E3.place(x = 150, y = 110)

    L4 = Label(top, text ="Pilihan Mobil")
    L4.pack(side = LEFT)
    L4.place(x = 10, y = 140)
    E4 = Entry(top, bd = 5)
    E4.pack(side = RIGHT)
    E4.place(x = 150, y = 140)

    L5 = Label(top, text = "Durasi")
    L5.pack(side = LEFT)
    L5.place(x=10, y = 170)
    E5 = Entry(top, bd = 5)
    E5.pack(side = RIGHT)
    E5.place(x=150, y = 170)

    def hasil_masukan():
        durasi = E5.get()
        mobil = E4.get()
        nama = E1.get()
        alamat = E2.get()
        no_telp = E3.get()
        harga = mobil * int (durasi)
        print (E1.get())
        print (E2.get())
        print (E3.get())
        if mobil == 'Jazz':
            harga = 300000 * int (durasi)
            print("Harga : Rp ",harga)
        elif mobil == "BMW":
            harga = 600000* int (durasi)
            print("Harga : Rp ",harga)
        elif mobil == "Innova":
            harga = 400000* int (durasi)
            print("Harga : Rp ",harga)
        elif mobil == "Pajero":
            harga = 700000* int (durasi)
            print("Harga : Rp ",harga)
        elif mobil == "Avanza":
            harga = 100000* int (durasi)
            print("Harga : Rp ",harga)
        else:
            print ("Maaf Kendaraan Tidak Tersedia")

        msg = messagebox.showinfo('AUTO RENTAL CAR',('Nama Lengkap : '+ nama,'\nAlamat Peminjam : ',alamat,'\nNo Telp : '+ no_telp,
                                                     '\nPilihan Mobil : '+ mobil,'\nDurasi Peminjaman : ' + durasi))

d
    button3 = Button(top, text = "Finish", command = hasil_masukan)
    button3.pack()
    button3.place(x = 150, y = 200)

def cek_car():
    
    top = Toplevel()

    header = Frame(top, bg = "red",height = 30)
    header.pack(side = TOP, fill = X)

    header = Frame(top, bg = "blue",height = 30)
    header.pack(side = BOTTOM, fill = X)
    
    top.title ("Auto Rental Car")
    top.geometry("300x200")
    label = Label(top, text ="Identitas Kendaraan")
    label.pack()

    L5 = Label(top, text ="Nama Peminjam")
    L5.pack(side = LEFT)
    L5.place(x = 10, y = 50)
    E5 = Entry(top, bd = 5)
    E5.pack(side = RIGHT)
    E5.place(x = 150, y = 50)
    
    L6 = Label(top, text ="Masukan Nama Mobil")
    L6.pack(side = LEFT)
    L6.place(x = 10, y = 80)
    E6 = Entry(top, bd = 5)
    E6.pack(side = RIGHT)
    E6.place(x = 150, y = 80)

    def data_peminjam():
        L7 = Label(top,text = "Nama Lengkap")
        L7.pack(side = LEFT)
        L7.place(x = 10, y = 50)
        x = E1.get()
        L8 = label(top,text = x)
        L8.pack(side = RIGHT)
        L8.place(x =150, y = 50)
    button4 = Button(top, text ="Cek",command = data_peminjam)
    button4.pack()
    button4.place(x = 150, y = 120)
    
def menu():
    root = Tk()

    header = Frame(root, bg = "red",height = 30)
    header.pack(side = TOP, fill = X)

    header = Frame(root, bg = "blue",height = 30)
    header.pack(side = BOTTOM, fill = X)


    root.title("Auto Rental Car")
    root.geometry("300x200")

    label = Label(root, text = "Selamat Datang \nPilih Menu Yang Tersedia\n")
    label.pack()
    button1 = Button(root, text = "Sewa", command = pilih_mobil)
    button1.pack()
    button1.place(x =133, y = 70)
    button2 = Button(root, text = "Kembalikan", command = cek_car)
    button2.pack()
    button2.place(x = 115, y = 100)
    button3 = Button(root, text ="Pernyaratan", command = persyaratan)
    button3.pack()
    button3.place(x =115, y = 130)
    root.mainloop()
menu()
