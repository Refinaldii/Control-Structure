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