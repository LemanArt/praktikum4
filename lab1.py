data=[]

while True:
   nama =input("Nama : ")
   nim = input("NIM : ")
   nTugas=int(input("Nilai Tugas : "))
   nUTS = int(input("Nilai UTS : "))
   nUAS = int(input("Nilai UAS : "))
   nilaiAkhir= (nTugas * 0.30) + (nUTS * 0.35) + (nUAS * 0.35)
   
   data.append([nama, nim, nTugas, nUTS, nUAS, nilaiAkhir])
   tambah = input ("Tambah data (y/t)?")
   if(tambah =="t"):
    break
print (74*"=")
print ("|No.|        Nama      |    NIM    | Tugas |  UTS  |  UAS  | Nilai Akhir |")
print (74*"=")
i=0
for a in data:
	i+=1
	print("|{no:2d} | {nama:16s} | {nim:9s} | {nTugas:5d} | {nUTS:5d} | {nUAS:5d} | {nilaiAkhir:11.2f} |"
		.format(no=i, nama=a[0], nim=a[1], nTugas=a[2], nUTS=a[3], nUAS=a[4], nilaiAkhir=a[5]))
print (74*"=")
