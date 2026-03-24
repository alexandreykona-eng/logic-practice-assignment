#Alex Andreyko
#3/24/2026

#1
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are eligible to vote.")
else:     
    print("You are not eligible to vote.") 

#2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1} == {num2}: {num1 == num2}")
print(f"{num1} != {num2}: {num1 != num2}")
print(f"{num1} < {num2}: {num1 < num2}")
print(f"{num1} > {num2}: {num1 > num2}")
print(f"{num1} <= {num2}: {num1 <= num2}") 
print(f"{num1} >= {num2}: {num1 >= num2}") 

#3
score = float(input("Enter test score (0-100): "))
attendance = float(input("Enter your attendance percentage (0-100)"))

if score >= 70 and attendance >= 80: 
    print("You pass the course.") 
else:
    print("You do not pass the course.") 

#4
s_id = input("Do you have a student ID? (yes/no): ").lower() 
l_card = input("Do you have a library card? (yes/no): ").lower() 
if s_id == "yes" or l_card == "yes": 
    print("You may enter the library.") 
else:     
    print("Access denied. You need a student ID or library card.") 

#5
banned = input("Are you banned from the system? (yes/no): ").lower() 
if not banned == "yes": 
    print("You may access the system.") 
else:     
    print("Access denied due to ban.") 

#6
gpa = float(input("Enter your GPA: ")) 
volunteer_hours = int(input("Enter your volunteer hours: ")) 
leadership = input("Do you hold a leadership role? (yes/no): ").lower() 
if gpa >= 3.5 and (volunteer_hours >= 50 or leadership == "yes"): 
    print("You qualify for the scholarship.") 
else:     
    print("You do not qualify for the scholarship.") 

