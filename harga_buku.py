def harga_bayaran(jenisbuku,kuantiti):
    harga_buku = {
        1: 25.00,
        2: 30.00,
        3: 35.00
    }
    
    harga_per_buku = harga_buku[jenisbuku]
    
    total_harga = harga_per_buku * kuantiti
    
    if kuantiti >= 5:
        potongan_harga = total_harga * 0.10
    else:
        potongan_harga = 0.00
        
    harga_total = total_harga - potongan_harga

    return potongan_harga, harga_total

def main():
    print("Senarai belian buku:")
    print("1.Latihan Pasti A,Bahasa Melayu,Tingkatan 1")
    print("2.Latihan Pasti A,Bahasa Melayu,Tingkatan 2")
    print("3.Latihan Pasti A,Bahasa Melayu,Tingkatan 3")
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break # exit when no error 
    kuantiti=int(input("Masukkan kuantiti buku yang dibeli:"))
    potongan_harga,harga_total = harga_bayaran(jenisbuku,kuantiti)
    print("Potongan harga yang diperoleh ialah RM", round(potongan_harga,2))
    print("Jumlah harga yang perlu dibayar ialah RM", round(harga_total,2))
    
if __name__ == "__main__":
    main()
