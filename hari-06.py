# list dasar

buah = ["apel","jeruk","mangga"]
print(buah[0])
print(buah[1])
print(buah[2])
print(f"Total buah: {len(buah)}")

# # ketika ingin menambah list di akhir
buah.append("pisang")
print(buah)

# # hapus sebagian item
buah.remove("apel")
print(buah)

# # cek keberadaan buah
print("durian" in buah)

# # urutkan list
buah.sort
print(buah)

# looping
for i in buah:
    print(f"saya suka buah {i}")

# dengan index
for i, b in enumerate(buah):
    print(f"{i+1}. buah {b}")

# DICTIONARY

mahasiswa = {
    "Nama" : "Asta",
    "Semester" : 7,
    "Jurusan" : "Informatika"
}
print(f"Nama : {mahasiswa["Nama"]}")



# Looping Dictionary
for a, b in mahasiswa.items():
    print(f"{a}: {b}")

# combine list and dictionary
KeluargaX = [
    {"Nama":"Nay","Umur":"45 Tahun"},
    {"Nama":"Kay","Umur":"50 Tahun"},
    {"Nama":"Mey","Umur":"20 Tahun"}
]

for k in KeluargaX:
    print(f"{k["Nama"]} {k["Umur"]}")

# latihan

belanja = []
print("Ketik 'Selesai' jika Sudah!")
while True :
    item = input("Masukan Item: ")
    if item == "selesai":
        break
    belanja.append(item)

print("\nDaftar item yang kamu masukan\n")
for i, b in enumerate():
    print(f"{i + 1}. {b}")


