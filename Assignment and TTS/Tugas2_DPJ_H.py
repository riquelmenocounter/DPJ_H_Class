def menu():
    print("===== MENU PILIHAN =====")
    print("1. Input tinggi segitiga")
    print("2. Deteksi ganjil/genap")
    print("3. FizzBuzz")
    print("4. Exit")

def tinggi_segitiga():
    while True:
        try:
            n = int(input("Masukkan Tinggi Segitiga: "))

        except ValueError:
            print("Input harus berupa angka!")
            continue

        for i in range(1, n+1):
            print(" *" * i)

        ulang = input("Input Lagi? (y/n): ").lower()
        if ulang != 'y':
            break

def ganjil_genap():
    while True:
        try:
            n = int(input("Masukkan Angka: "))

        except ValueError:
            print("Input harus berupa angka!")
            continue

        number = n
        if number % 2 == 0:
            print(f"{number} adalah GENAP")
        else:
            print(f"{number} adalah GANJIL")

        ulang = input("Input Lagi? (y/n): ").lower()
        if ulang != 'y':
            break

def fizzBuzz():
    while True:
        try:
            n = int(input("Masukkan Batas Angka: "))

        except ValueError:
            print("Input harus berupa angka!")
            continue

        batas = n
        for i in range(1, batas+1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            # Jika kelipatan 5
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)

        ulang = input("Input Lagi? (y/n): ").lower()
        if ulang != 'y':
            break

while True:
    menu()
    try:
        n = int(input("Masukkan Pilihan: "))

    except ValueError:
        print("Input harus berupa angka!")
        continue

    pilihan = n

    if pilihan == 1:
        tinggi_segitiga()
    elif pilihan == 2:
        ganjil_genap()
    elif pilihan == 3:
        fizzBuzz()
    elif pilihan == 4:
        print("Terima kasih, Semangat mengerjakan!")
    else:
        print("Pilihan tidak valid. Silakan pilih 1-4.")
        break
