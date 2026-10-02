import csv
#reading the whole file at one
with open("./files/test.txt", "r") as text_file:
  content = text_file.read()
  print(content) 

#reading the file line by line

""" with open("./files/test.txt", "r") as text_file:
  for line in text_file:
    print(line.strip()) """ 

with open("./files/text.text", "r") as text_file:
  line = text_file.readline()
  lines = text_file.readlines()
  print(line)
  print(lines)
  print(text_file.tell())
  text_file.seek(5)
  print(text_file.tell())
  print(text_file.read(20))

#CSV
with open("./files/student.cvs", "r") as file:
  reader = csv.reader(file)
  header = next(reader)
  print(f"Header: {header}")

  for row in reader:  
    print(row)

#CSV dictionary
with open("./files/student.cvs", "r") as file:
  reader = csv.DictReader(file)
  for student in reader:  
    cgpa = float(student["cgpa"])
    if cgpa > 4.5:
      print(student["name"])
    



 








