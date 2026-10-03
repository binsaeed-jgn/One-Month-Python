

try:
  number_1 = int(input("enter an integer number"))
  number_2 = int(input("enter an integer number"))
  division = number_1/number_2
  print(division)
except ValueError as error :
  print("You enter invalid number\nPlease enter an integer number", error)
except ZeroDivisionError as error :
  print("You cannot divide by zero", error)
else:
  print("Sucessfully")
finally:
  print("Finished")









