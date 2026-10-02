import csv
with open ("./files/text.text", "w") as file:
  file.write("Name: bashir")

""" with open("./files/student.txt", "w") as file:
  file.write("Name: Bahs\n")
  file.write("School: wamy\n")
  file.write("class: ss2\n")

with open("./files/student.txt", "a") as file:
  file.write("cGPA: 5:00\n")

with open("./files/student.txt", "a") as file:
  file.write("title: legend")

with open("./files/student.txt", "r") as file:
  for line in file:
    print(line.strip())
 """
student = {
  "name":" Bash",
  "versity": "Buk",
  "level": "300",
  "dept": "SWE"

}

with open("./files/student.txt", "w") as file:
  file.write(f"Name {student['name']}\n")
  file.write(f"versity {student['versity']}\n")
  file.write(f"Level {student['level']}\n")
  file.write(f"Dept {student['dept']}\n\n")

with open("./files/student.txt", "a") as file:
  file.write("Name: Bukhar\n")
  file.write("School: wamy\n")
  file.write("class: ss2\n")

with open("./files/student.txt", "a") as file:
  file.write("cGPA: 5:00\n")

with open("./files/student.txt", "a") as file:
  file.write("title: legend\n\n")

with open("./files/student.txt", "r") as file:
  for line in file:
    print(line.strip())

#Cvs
with open("./files/student.cvs", "w") as file:
  readerc= csv.reader(file)
