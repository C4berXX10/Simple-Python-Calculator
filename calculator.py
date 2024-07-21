def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   if y == 0:
       return "Error! Division by zero is not allowed."
   else:
       return x / y

print(" Calculator ")
print("a.Plus (+)")
print("b.Minus (-)")
print("d.Multiply (×)")
print("c.Divide (÷)")

print (" ")

while True:
   choice = input("Choose One :- ")

   if choice in ('a', 'b', 'c', 'd') :
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))

       if choice == 'a':
           print(num1, "+", num2, "=", add(num1, num2))

       elif choice == 'b':
           print(num1, "-", num2, "=", subtract(num1, num2))

       elif choice == 'c':
           print(num1, "*", num2, "=", multiply(num1, num2))

       elif choice == 'd':
           print(num1, "/", num2, "=", divide(num1, num2))
       break
   else:
       print("Invalid Input")
