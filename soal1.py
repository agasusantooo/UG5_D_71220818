def ganti_kata(kalimatlama, carikata, kataganti):
    kata = ""
    kalimatbaru = ""
    for i in range(len(kalimatlama)):
        if kalimatlama[i] == " ":
            if kata == carikata:
                kalimatbaru += kataganti + " "
            else:
                kalimatbaru += kata + " "
            kata = ""
        elif i == len(kalimatlama) - 1:
            kata += kalimatlama[i]
            if kata == carikata:
                kalimatbaru += kataganti
            else:
                kalimatbaru += kata
        else:
            kata += kalimatlama[i]
    return kalimatbaru

kalimatlama = input("Masukkan kalimat: ")
carikata = input("Masukkan kata yang ingin diganti: ")
kataganti = input("Masukkan kata pengganti: ")

kalimatbaru = ganti_kata(kalimatlama, carikata, kataganti)

print("Kalimat baru:", kalimatbaru)
