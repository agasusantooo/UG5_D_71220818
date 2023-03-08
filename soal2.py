def hitung_mobil():
    
    solo=0
    surabaya=0
    jogja=0
    magelang=0
    while True:
        kotaasal=input("Masukkan asal mobil (ketik \"done\" untuk keluar) : ").lower()
        if kotaasal == "solo":
            solo+=1
        elif kotaasal == "surabaya":
            surabaya+=1
        elif kotaasal == "jogja":
            jogja+=1
        elif kotaasal == "magelang":
            magelang += 1
        elif kotaasal == "done":
            break
        else:
            print("Asal kota tidak terdaftar")
    print("Jumlah Mobil Solo        : ",solo)
    print("Jumlah Mobil Surabaya    : ",surabaya)
    print("Jumlah Mobil Jogja       : ",jogja)
    print("Jumlah Mobil Magelang    : ",magelang)


hitung_mobil()
