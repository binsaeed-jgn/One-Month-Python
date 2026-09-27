from functools import reduce
double = lambda x : x*2
add = lambda a,b : a + b
sub = lambda a,b=0: a-b
isEven = lambda num: num%2==0

print(double(5))
print (add(5,6))
print(sub(5)) # uisng default parameter
print(sub(5,4))
print(isEven(81))

# lambda and map
numbers = [1,2,3,4,5,6,7,8,9,10]
def even(n):
  return n%2 ==0


double = map(lambda x: x**2, numbers)
print(list(double))

#filter 
even_num = filter(lambda x: x%2==0, numbers)
print(f"Even Numbers: {list(even_num)}")

odd_num = filter(lambda x: x%2!=0, numbers)
print(f"Odd Numbers: {list(odd_num)}")

# filter using function 
count = [10,11,12,13,14,15,16,17,18,19,10]
even_num_2 = filter(even, count)
result = list(even_num_2)
print(f"Even Numbers: {(result)}")
print(f"Even Numbers: {sum(result)}")

#using list comprehension
# [expression, collection, condition]

numbers_2 = [1,2,3,4,5,6]
sum_even = [num for num in numbers_2 if num%2==0 ]
print(sum(sum_even))

#dictionary comprehension {key:  value  for item in collection condtion}
dic_numbers = [1,2,3,4,5,6]
dic_squares = {numb:numb**2 for numb in dic_numbers}
print(f"Dictionary_Square{dic_squares}")

dic_even_square =  {numb:numb**2 for numb in dic_numbers if numb%2==0 }
print(f"Dictionary_Even_Square{dic_even_square}")

 
