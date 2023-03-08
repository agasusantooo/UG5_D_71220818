from math import tan, radians
while True:
    jarak1 = input("Masukkan jarak awal (dalam meter): ")
    if jarak1 == "berhenti" or jarak1 == "stop":
        print("Program dihentikan")
        break
    sudutmenitke5 = float(input("Masukkan sudut elevasi pada menit ke-5 (dalam derajat): "))
    sudutmenitke6 = float(input("Masukkan sudut elevasi pada menit ke-6 (dalam derajat): "))
    
    tinggi = float(jarak1) * tan(radians(sudutmenitke5))
    jarak2 = float(jarak1) * tan(radians(sudutmenitke6)) - float(jarak1) * tan(radians(sudutmenitke5))
    selisihketinggian = jarak2 * tan(radians(sudutmenitke6))
    
    print(f"Ketinggan drone pada menit ke-5 adalah {tinggi:.2f} meter")
    print(f"Jarak helikopter secara vertical {selisihketinggian:.2f} meter")
