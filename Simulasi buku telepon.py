def aplikasi_buku_telepon():
    kontak = {}

    while True:
        print("\n=== MENU KONTAK ===")
        print("1. Tambah")
        print("2. Cari")
        print("3. Lihat Semua")
        print("4. Hapus")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":

            # INPUT NAMA (WAJIB VALID)
            while True:
                nama = input("Nama kontak: ").strip()
                if nama == "":
                    print("Nama tidak boleh kosong.")
                elif nama.isdigit():
                    print("Nama tidak boleh angka semua.")
                else:
                    break

            # INPUT NOMOR (WAJIB ANGKA)
            while True:
                nomor = input("Nomor HP: ").strip()
                if nomor == "":
                    print("Nomor tidak boleh kosong.")
                elif not nomor.isdigit():
                    print("Nomor harus angka saja.")
                else:
                    break

            kontak[nama] = nomor
            print("Kontak berhasil disimpan.")

        elif pilihan == "2":
            nama = input("Masukkan nama yang dicari: ").strip()
            if nama in kontak:
                print("Nama  :", nama)
                print("Nomor :", kontak[nama])
            else:
                print("Kontak tidak ditemukan.")

        elif pilihan == "3":
            if not kontak:
                print("Belum ada kontak.")
            else:
                print("Daftar Kontak:")
                for i, (nama, nomor) in enumerate(kontak.items(), start=1):
                    print(f"{i}. {nama} - {nomor}")

        elif pilihan == "4":
            nama = input("Masukkan nama yang ingin dihapus: ").strip()
            if nama in kontak:
                del kontak[nama]
                print("Kontak berhasil dihapus.")
            else:
                print("Nama tidak ditemukan.")

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")

aplikasi_buku_telepon()