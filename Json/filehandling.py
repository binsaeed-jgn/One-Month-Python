import json

# 1. READ FROM FILE (With safety check for empty files)
try:
    with open("student.json", "r") as file:
        students = json.load(file)
        
    for student in students:
        # Print only those with first class (> 4.0) name and last skill
        cgpa = float(student['cgpa'])
        if cgpa > 4.00:
            # Check if skills list exists and is not empty before indexing
            if "skills" in student and student["skills"]:
                print(f"{student['name']}  Skills: {student['skills'][-1]}")
            else:
                print(f"{student['name']}  Skills: No skills listed")

except json.decoder.JSONDecodeError:
    print("Warning: student.json was empty or broken! Creating new data...")
    students = [] # Start with an empty list if file was broken


# 2. WRITE NEW DATA TO FILE
# Note: Added the 'skills' back here so your next read won't fail!
new_students_list = [
  {"name": "Isah", "dept": "SWE", "level": 100, "cgpa": 3.7, "skills": ["python", "html", "css"]},
  {"name": "Adam", "dept": "CBY", "level": 200, "cgpa": 3.99, "skills": ["python", "html", "css"]},
  {"name": "Ahmad", "dept": "CSC", "level": 300, "cgpa": 5.00, "skills": ["python", "html", "css"]},
  {"name": "Bash", "dept": "IT", "level": 400, "cgpa": 4.79, "skills": ["python", "html", "css"]}
]

with open("student.json", "w") as file:
    json.dump(new_students_list, file, indent=2)
