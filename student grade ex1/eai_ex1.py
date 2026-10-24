name = input("Enter student name: ") 
n = int(input("Enter number of subjects: ")) 

while n <= 0:
    print("Invalid input! Number of subjects must be greater than zero.")
    n = int(input("Enter a valid number of subjects: "))

total = 0 
for i in range(1, n + 1): 
    mark = float(input(f"Enter mark for Subject {i}: ")) 
    total += mark 
    
percentage = total / n 

if percentage >= 90: 
    grade, performance = "A+", "Outstanding" 
elif percentage >= 80: 
    grade, performance = "A", "Excellent" 
elif percentage >= 70: 
    grade, performance = "B", "Very Good" 
elif percentage >= 60: 
    grade, performance = "C", "Good" 
elif percentage >= 50: 
    grade, performance = "D", "Average" 
else: 
    grade, performance = "F", "Needs Improvement" 
    
print("\n\t\t Academic Performance \t\t")
print("Student Name :", name) 
print("Total Marks :", total) 
print("Percentage :", round(percentage, 2), "%") 
print("Grade :", grade) 
print("Performance :", performance)