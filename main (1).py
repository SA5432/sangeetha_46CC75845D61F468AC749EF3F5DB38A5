#1.1 Implememt a recursive to calculate the given factorial number
def fact(n):
  if n==0:
    return 1
  else:
    return n*fact(n-1)
print("\n factorial of a number") 
num=int(input("enter a non-negative integer:"))
factorial=fact(num)
print("the factorial of",num, "is",factorial) 