# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# Expected Output:

# [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]


def list(a,b):
     for e in range(4,31):
          if e%2==0:
               sum=[e]
               print(sum,end="")


list(4,30)
  