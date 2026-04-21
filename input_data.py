def ambil_data(): 
    nama = input("Masukkan nama mahasiswa: ") 
    nilai = [] 
    
    for i in range(3): 
        n = float(input(f"Masukkan nilai ke-{i+1}: ")) 
        nilai.append(n)
        
return nama, nilai