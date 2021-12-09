import math
def prime_checker(number):
  square = round(math.sqrt(number))

  result = "It's a prime number."
  for n in range(1, square):
    if number % n == 0:
      result = "It's not a prime number."
  
  print(result)


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)