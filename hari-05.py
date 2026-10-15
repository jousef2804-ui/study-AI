# belajar for loop dan while
# 
# hitung maju
angka=int(input("Masukan Angkamu Disini: "))
for i in range(1,11):
    print(f"{angka} x {i} = {angka*i}")


# hitung mundur
angka=int(input("Masukan Angka Disini: "))
for i in range (angka,0,-1):
    print(i)
print("Go!")

# tebak angka
x=7
y=0

while True:
    tebakan = int(input("Tebak Angka (1-15): "))
    y=y+1
    if tebakan == x :
        print(f"Bravo! kamu benar, dan kamu udah menebak sebanyak {y} kali")
        break
    elif tebakan <= 3:
        print("Tebakanmu terlalu kecil")
    elif tebakan > 3 and tebakan < 10:
        print("Tebakanmu hampir benar")
    else:
        print("Tebakanmu Terlalu besar")

print("=== Kalkulator sederhana ===\nketik 'Quit' untuk keluar")

while True :
    angka1 = input("Masukan Angka Pertama = ")
    if angka1 == "quit":
        print("Sampai Jumpa!")
        break
    
    angka1 = float(angka1)
    operator = input("Masukin operator (+,-,x,:) = ")
    angka2 = float(input("Masukan Angka Kedua = "))
    if operator == "+" :
        hasil = angka1 + angka2
    elif operator == "-" :
        hasil = angka1 - angka2
    elif operator == "x" :
        hasil = angka1 * angka2
    else:
        hasil = angka1 / angka2
    
    print(f"Hasil {angka1:g} {operator} {angka2:g} = {hasil:g}") #":g" itu gunanya biar angka desimal jadi general alias bulat