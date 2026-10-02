 
#collect name & greet
name = input("Enter Your name: ")
def greet():
  print(f"Welcome {name}")
greet()

#local and global
def intro():
  name = "Hassan"
  print(f"local name :{name}")
print(f"global name:  {name}")
intro()

#parameters 
def add(a,b):
  return a + b
print(add(5,10))

#default parameter
def total(price, quan=1 ):
  print (quan * price)

total(5) 
total(5,3)

# argument 
def add_all(*num):
  return sum(num)

print(add_all(1,3,4))
print(add_all(5,6,7,8,9))

def skills(*skills):
  for skill in skills:
    print(skill)

skills("py", "js", "React")

#kwargs

def student_info(**data):
  for key, value in data.items():
    print(key, ":", value)

student_info(
  name="anna",
  level=300,
  school= "wamy"

)
