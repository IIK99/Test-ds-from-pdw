# pasar buah tanpa def function
# Daftar buah
fruits = [
    {"nama": "apel", "stock": 20, "harga": 10000},
    {"nama": "jeruk", "stock": 15, "harga": 8000},
    {"nama": "anggur", "stock": 25, "harga": 15000},
]

while True:
    print("Selamat datang di pasar buah")
    print("List menu:")
    print("1. Menampilkan daftar buah")
    print("2. Menambah buah")
    print("3. Menghapus buah")
    print("4. Membeli buah")
    print("5. Exit program")
    print()

    choice = int(input("Masukkan angka menu yang ingin dijalankan: "))

    if choice == 1:
        print("Index\t|Nama\t|Stock\t|Harga")
        for index, fruit in enumerate(fruits):
            print(f"{index}\t|{fruit['nama']}\t|{fruit['stock']}\t|{fruit['harga']}")
        print()

    elif choice == 2:
        nama = input("Masukkan nama buah: ")
        stock = int(input("Masukkan stock buah: "))
        harga = int(input("Masukkan harga buah: "))
        fruits.append({"nama": nama, "stock": stock, "harga": harga})

    elif choice == 3:
        print("Index\t|Nama\t|Stock\t|Harga")
        for index, fruit in enumerate(fruits):
            print(f"{index}\t|{fruit['nama']}\t|{fruit['stock']}\t|{fruit['harga']}")
        print()
        index = int(input("Masukkan index buah yang ingin dihapus: "))
        if 0 <= index < len(fruits):
            fruits.pop(index)
        else:
            print("Index tidak valid.")

    elif choice == 4:
        print("Index\t|Nama\t|Stock\t|Harga")
        for index, fruit in enumerate(fruits):
            print(f"{index}\t|{fruit['nama']}\t|{fruit['stock']}\t|{fruit['harga']}")
        print()
        index = int(input("Masukkan index buah yang ingin dibeli: "))
        if 0 <= index < len(fruits):
            quantity = int(input("Masukkan jumlah yang ingin dibeli: "))
            if quantity <= fruits[index]["stock"]:
                total_harga = quantity * fruits[index]["harga"]
                fruits[index]["stock"] -= quantity
                print(
                    f"Anda telah membeli {quantity} {fruits[index]['nama']} dengan total harga {total_harga}"
                )
            else:
                print("Stock tidak mencukupi.")
        else:
            print("Index tidak valid.")

    elif choice == 5:
        print("Terima kasih telah menggunakan pasar buah!")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
