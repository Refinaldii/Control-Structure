#Task 4. Program Python untuk Mencetak Bilangan Ganjil Hingga n
n = int(input("Masukkan batas atas: "))  # Input batas atas hingga n

for i in range(1, n + 1):  # Loop dari 1 hingga n
    if i % 2 != 0:  # Jika i adalah bilangan ganjil
        print(i, end=" ")  # Cetak bilangan ganjil