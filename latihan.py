a=[1,2,3,4,5]
print (a)
print("===AKSES LIST===")

print(a[3])
print(a[1:4])
print(a[4])

print("===UBAH ELEMEN LIST===")
a[3] = 6
print(a)
a[3:-1] = [7,8]
print(a[0:-1])
print("===TAMBAH ELEMEN LIST===")
b=[]
b.append(a[0:-4])
b.extend(["ini","ibu", "budi"])
print(b)
print("=====Gabungan list====")
list = a + b
print(list)