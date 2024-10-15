##Task 1
# Get the student's percentage from the user
percentage = float(input("Enter the student's percentage: "))

# Evaluate the student's performance
if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Needs improvement")

#Task 2
# Get the three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)

#Task 3
n = int(input("Masukkan batas bilangan Fibonacci: "))  # Input batas bilangan Fibonacci yang diinginkan

a, b = 0, 1  # Inisialisasi dua elemen pertama Fibonacci
while a <= n:  # Loop hingga nilai a melebihi n
    print(a, end=" ")  # Cetak nilai a saat ini
    a, b = b, a + b # Update nilai a dan b untuk elemen berikutnya
print ("\n") 

#Task 4
n = int(input("Masukkan batas atas: "))  # Input batas atas hingga n

for i in range(1, n + 1):  # Loop dari 1 hingga n
    if i % 2 != 0:  # Jika i adalah bilangan ganjil
        print(i, end=" ")  # Cetak bilangan ganjil
print ("\n")

#Task 5

n = int(input("Masukkan nilai n: "))  # Input nilai n sebagai batas pola

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

