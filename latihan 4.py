list = []
nomer  = 0
while True:
    nim = input("Masukan Nim : ")
    nama = input("Masukan Nama : ")
    nilaitugas = int(input("masukan nilai tugas : "))
    uts = int(input("masukan nilai uts : "))
    uas = int(input("masukan nilai uas : "))
    akhir = (nilaitugas*.3 + uts*.35 + uas*.35)
    nomer+=1
    list.append([nomer, nim, nama, nilaitugas, uts, uas, akhir])
    ulangi = input("Tambah data (y/t)? ")
    if ulangi == "t":
        break;

print("\nDAFTAR NAMA\n")
print("=======================================================================================")
print("|   NIM   |   Nama   |   Nilai Tugas   |   Nilai UTS   |   Nilai UAS   |   Akhir      |")
print("=======================================================================================")
for i in list:
    print ("| {0:7d} | {1:8s} | {2:15s} | {3:13d} | {4:13d} | {5:6d} | {6} |".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
print("=======================================================================================")