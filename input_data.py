def ambil_data():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = []

    for i in range(3):
        while True:
            try:
                n = float(input(f"Masukkan nilai ke-{i+1}: "))
                if 0 <= n <= 100:
                    nilai.append(n)
                    break
                else:
                    print("Nilai harus antara 0 - 100!")
            except ValueError:
                print("Input harus angka!")

    return nama, nilai