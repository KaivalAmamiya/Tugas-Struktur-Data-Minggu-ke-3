def hapus_duplikat(data):
    return list(dict.fromkeys(data))

# Contoh
angka = [1,2,2,3,4,3,5]
print(hapus_duplikat(angka))