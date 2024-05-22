# find min and max values numbers
numbers = [41, 5, 1, 3, 89, 32]

min = numbers[0]
max = numbers[0]
print(min, max)

for number in numbers:
    if number < min:
        min = number

print(min)

for number in numbers:
    if number > max:
        max = number

print(max)

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# pasar buah
def display_menu():
    print("Selamat datang di pasar buah")
    print("List menu:")
    print("1. Menampilkan daftar buah")
    print("21. Menambah buah")
    print("3. Menghapus buah")
    print("4. Membeli buah")
    print("5. Exit program")
    print()


def display_fruits(fruits):
    print("Index\t|Nama\t|Stock\t|Harga")
    for index, fruit in enumerate(fruits):
        print(f"{index}\t|{fruit['nama']}\t|{fruit['stock']}\t|{fruit['harga']}")
    print()


def add_fruit(fruits):
    nama = input("Masukkan nama buah: ")
    stock = int(input("Masukkan stock buah: "))
    harga = int(input("Masukkan harga buah: "))
    fruits.append({"nama": nama, "stock": stock, "harga": harga})


def remove_fruit(fruits):
    display_fruits(fruits)
    index = int(input("Masukkan index buah yang ingin dihapus: "))
    if 0 <= index < len(fruits):
        fruits.pop(index)
    else:
        print("Index tidak valid.")


def buy_fruit(fruits):
    display_fruits(fruits)
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


def main():
    fruits = [
        {"nama": "apel", "stock": 20, "harga": 10000},
        {"nama": "jeruk", "stock": 15, "harga": 8000},
        {"nama": "anggur", "stock": 25, "harga": 15000},
    ]

    while True:
        display_menu()
        choice = int(input("Masukkan angka menu yang ingin dijalankan: "))
        if choice == 1:
            display_fruits(fruits)
        elif choice == 2:
            add_fruit(fruits)
        elif choice == 3:
            remove_fruit(fruits)
        elif choice == 4:
            buy_fruit(fruits)
        elif choice == 5:
            print("Terima kasih telah menggunakan pasar buah!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
