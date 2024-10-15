n = int(input("Masukkan nilai n: "))  # Input nilai n sebagai batas pola

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()