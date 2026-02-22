def cari_irisan(list_a, list_b):
    hasil = []
    for elemen in list_a:
        if elemen in list_b and elemen not in hasil:
            hasil.append(elemen)
    return hasil

# Contoh
print(cari_irisan([1,2,3,4], [3,4,5,6]))