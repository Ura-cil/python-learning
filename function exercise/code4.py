# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() with the following specifications:

# It should accept the employee’s name and salary.
# It should display both the name and salary.
# If the salary is not provided in the function call, it should default to 9000.
# See: Default arguments in function


# Given:
# showEmployee("Ben", 12000)

# showEmployee("Jessa")

def showEmployee(name, salary=9000):# for default value we give the value in function of an argument

    print(name, salary)

if __name__ == "__main__":

   showEmployee("Ben", 12000)
   showEmployee("Jessa")



