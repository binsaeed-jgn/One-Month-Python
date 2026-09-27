
student_info = {
  "name": "Hafsah",
  "Unversity": "S.Zungur",
  "CGPA": 5.00,
  "level": 400,
  "course": "Nurse"
}

print(student_info["name"])
print(student_info["CGPA"])
student_info["skill"] = "cooking"

for key, value in student_info.items():
  print(key, ":", value)


#Nested Dictionary

students = {
  "student_1" :{
    "name": "Bashir",
    "Unversity": "BUK",
    "CGPA": 4.00,
    "level": 300,
    "course": "Software Engineering"
  },
  "student_2" : {
    "name": "Nana",
      "Unversity": "S.Zungur",
      "CGPA": 5.00,
      "level": 400,
      "course": "Nurse"
  }

}

for key, value in students["student_1"].items():
  print(key, ";", value)


#list Dictionary 
student_1 ={
    "name": "Bashir",
    "Unversity": "BUK",
    "CGPA": 4.00,
    "level": 300,
    "course": "Software Engineering"
  }
student_1["skills"] = ["Github", "React", "Python"]
print(student_1)
#for value in student_1["skills"].values():
print(student_1["skills"])

for x in student_1["skills"]:
  print(x)

