
try:
  with open("student.txt" "r") as file:
    content = file.read()
    print(content)
except FileNotFoundError as error:
  print("file do not exist", error)

#CGPA Challenge
try:
  cgpa = float(input("Enter your CGPA"))

  if (cgpa >= 4.5):
    print(f"Your CGPA is: {cgpa}. You are a first class.")
  elif (cgpa >= 3.5):
    print(f"Your CGPA is: {cgpa}. You are a second class.")
except ValueError as error:
  print(f"You've entered invalid input", error)
else: 
  print(f"Your CGPA {cgpa} printed successfully")
finally:
  print(f"Program finished")
