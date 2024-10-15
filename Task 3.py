n = int(input("Masukkan batas bilangan Fibonacci: "))  # Input batas bilangan Fibonacci yang diinginkan

a, b = 0, 1  # Inisialisasi dua elemen pertama Fibonacci
while a <= n:  # Loop hingga nilai a melebihi n
    print(a, end=" ")  # Cetak nilai a saat ini
    a, b = b, a + b # Update nilai a dan b untuk elemen berikutnya
print ("\n") 