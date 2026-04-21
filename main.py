from input_data import ambil_data
from proses_nilai import hitung_rata_rata, cek_kelulusan

def main():
    nama, nilai = ambil_data()
    rata = hitung_rata_rata(nilai)
    status = cek_kelulusan(rata)

    print("\n=== HASIL ===")
    print("Nama:", nama)
    print("Nilai:", nilai)
    print("Rata-rata:", rata)
    print("Status:", status)

if __name__ == "__main__":
    main()