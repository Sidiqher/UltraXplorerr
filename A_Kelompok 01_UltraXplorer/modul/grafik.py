import csv
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


nilai = ["23","45","23",]

# Data contoh
def grafik(nilai):
    global fig
    nilai = nilai[0][1:]
    nilai_int = []
    for i in nilai:
        nilai_int.append(float(i))
    header = []
    for j in range(len(nilai)):
        header2 = "nilai" + str(j+1)
        header.append(header2)


    # Plotting nilai

    # Konfigurasi plot
    plt.title('Monitoring Nilai Quiz')
    plt.ylabel('Nilai')

    # Tampilkan plot

    fig = Figure(figsize=(7, 3), dpi=100)  
    ax = fig.add_subplot(111)  
    ax.plot(header, nilai_int, marker='o', linestyle='-', color='b')

if __name__=="__main":
    grafik(nilai)