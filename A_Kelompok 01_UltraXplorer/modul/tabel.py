from tabulate import tabulate

def tabel(data_nilai):
        global table
        angka = 0
        rata_rata = 0
        for i in data_nilai[0][1:]:
                angka = float(i) + angka
                rata_rata = angka/len(data_nilai[0][1:])
        data_nilai[0].append(str(rata_rata))
        header = ["mata kuliah","Nilai1", "Nilai2", "Nilai3","nilai4","nilai5"]
        header = header[0:len(data_nilai[0][1:])]
        header.append("Rata-rata")
        table = tabulate(data_nilai, headers=header, tablefmt="grid")


def tabel2(data_nilai):
        global table
        angka = 0
        rata_rata = 0
        for i in data_nilai[0][1:]:
                angka = float(i) + angka
                rata_rata = angka/len(data_nilai[0][1:])
        data_nilai[0].append(str(rata_rata))
        header = ["mata kuliah","Nilai UTS", "Nilai UAS"]
        header = header[0:len(data_nilai[0][1:])]
        header.append("Rata-rata")
        table = tabulate(data_nilai, headers=header, tablefmt="grid")