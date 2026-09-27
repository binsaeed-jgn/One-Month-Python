
name =  input("Enter your name ").strip()
title = input("Enter your title ").strip().title()

# name & title 
print(f"My name is: {name}  My title is: {title} ")

# name firt two letters
print(f"Name first two letters: {name[:2]} ")
print(f"Name last three letters: {name[-3:]}")
print(f"title jumping 2 letters: {title[0:-1:2]}")


""" name =  input("Enter your name ").strip()
title = input("Enter your title ").strip().title()

# name & title 
print(f"My name is: {name}  My title is: {title} ")

# name firt two letters
print(f"Name first two letters: {name[:2]} ")
print(f"Name last three letters: {name[-3:]}")
print(f"title jumping 2 letters: {title[0:-1:2]}") """

#Conditional

""" score = int(input("Enter your score: "))

if score > 100 or score < 0:
    print(f"{score} is invalid. Please enter a score between 0 and 100.")
elif score >= 70:
    print(f"Your Score is: {score}, Your Grade is A")
elif score >= 60:
    print(f"Your Score is: {score}, Your Grade is B")
elif score >= 50:
    print(f"Your Score is: {score}, Your Grade is C")
elif score >= 40:
    print(f"Your Score is: {score}, Your Grade is D")
else:
    print(f"Your Score is: {score}, Your Grade is F")

#Loop
for x in range(1,11):
    print(f"5 X {x} = {x*5}")

number = 10
while number > 0 :
    print(number)
    number -=1

for  x in range (1,21):
    if x%2==0:
        continue
    print (x) """


#List

student = ["Ahmad", "Ali", 45]
student.append(70)
student.insert(3, "Musa")
print (student)

#print individual list value

for s in student:
  print(s)

  names = ["Bahsir", "Ahmad", "Ali", "Umar"]
  names.append(90)
  names.insert(-2,"Musa")
  names.append("Imran")
  names.pop(-2)
names_copy = names.copy()
print(names)
print(names_copy[::-1])

#Tuple Immutable List

days = ("Monday", "Tuesday", "Wednessday","Thursday", "Friday")

print(days)

if "Sunday" in days:
  print("weekend")
else:
  print("working day")

colors = {"red", "blue","green", "orange"}
print(colors)
for color in colors:
  print(color)
username = ["Bashir", "Ali", "Bashir", "Ali"]
set_username = set(username)
print(set_username)



