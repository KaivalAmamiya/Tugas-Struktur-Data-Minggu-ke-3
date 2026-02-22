def karakter_berulang(teks):
    for i in range(len(teks)):
        for j in range(i + 1, len(teks)):
            if teks[i] == teks[j]:
                return teks[i]
    return None

# Contoh
hasil = karakter_berulang("abcaabcd")
print("Karakter pertama yang berulang:", hasil)