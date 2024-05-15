from PIL import Image, ImageDraw, ImageFont, ImageTk
import Program as md
import csv


# Fungsi untuk membuat ID card
def buat_id_card(name, nim, background_path, output_path):
    # Mengambil latar belakang
    background = Image.open(background_path)
    
    # Mengatur ukuran ID card
    lebar_kartu = 650
    tinggi_kartu = 1020
    
    # Membuat ID card kosong dengan latar belakang
    id_card = Image.new('RGB', (lebar_kartu, tinggi_kartu), (255, 255, 255))
    id_card.paste(background, (0, 0))
    
    # Mengatur jenis font teks
    font = ImageFont.truetype('times.ttf', 40)
    warna_text = (0, 0, 0)
    
    # Meletakan teks di ID card
    gambar = ImageDraw.Draw(id_card)

    # Mengukur lebar teks dan membuat teks center
    lebar_nama, _ = gambar.textsize(f"{name}", font=font)
    lebar_nim, _ = gambar.textsize(f"{nim}", font=font)

    text_x = int((lebar_kartu - lebar_nama) / 2)
    text_x2 = int((lebar_kartu - lebar_nim) / 2)
    text_y = 495
    line_spacing = 150
    
    gambar.text((text_x, text_y), f"{name}", font=font, fill=warna_text)
    gambar.text((text_x2, text_y + line_spacing), f"{nim}", font=font, fill=warna_text)
    
    # Simpan ID card ke file
    id_card.save(output_path)


# Menampilkan ID Card pada program
def tampilkan():
    global photo
    global photo2
    card = Image.open(f"databaseuser/{md.username_user}/idcard.png").convert("RGB") 
    size = (360,540) 
    card = card.resize(size)
    photo = ImageTk.PhotoImage(card)