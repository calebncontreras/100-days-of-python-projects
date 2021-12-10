# Calculator 

from replit import clear
from art import logo
#Add 
def Add(a, b):
  return a + b

#Subtract
def Subtract(a, b):
  return a - b

#Divide
def Divide(a, b):
  return a / b

#Multiply
def Multiply(a, b):
  return a * b

operations = {
  "+": Add,
  "-": Subtract,
  "*": Multiply,
  "/": Divide
}

def calculator():

  print(logo)

  num1 = float(input("What is your first number?: "))
  for symbol in operations:
    print(symbol)
  recalculate = True

  while recalculate:

    symbol = input("choose an operation: ")
    num2 = int(input("What is your next number?: "))

    calculation_function = operations[symbol]

    answer = calculation_function(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")

    keep_calc = input("Do you want to continue calcuting with the same number?: ")

    if keep_calc == "y":
      num1 = answer
    elif keep_calc == "n":
      recalculate = False
      clear()
      calculator()


calculator()