import json

with open("new_student.json", "r") as file:
  new_list = json.load(file)
  print(new_list) # print all the json
  print(f"Name: {new_list['name']}")# print name
  print(f"Name: {new_list['cgpa']}") # print cgpa
  print(f"Name: {new_list['skills'][1]}") # print first skills

  for skill in new_list['skills']: # all the skills using loop
    print(f"Skill: {skill}")
    

  
  

