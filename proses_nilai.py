def hitung_rata_rata(daftar_nilai):
    return sum(daftar_nilai) / len(daftar_nilai)

def cek_kelulusan(rata_rata):
    if rata_rata >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"