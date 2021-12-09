from replit import clear
#HINT: You can call clear() to clear the output in the console.
import pprint 

from art import logo

pp = pprint.PrettyPrinter(indent=4)
print(logo)


def find_highest_bidder(bidding_dict):
  highest_bid = 0
  winner = ""
  for key, value in bidding_dict.items():
    if value > highest_bid:
      highest_bid = value
      winner = key

  print(f"The highest bidder is {winner} at {highest_bid}")

# set loop flag
bidding_finished = False 

auction_dict = {}

while not bidding_finished:
  
  name = input("What is your name?: ")
  bid = int(input("How much would you like to bid?: "))
  
  # adding user name and bid to dict  
  auction_dict[name] = bid 

  # prompt user to continue the auction
  auction_continue = input("Do I hear another bid? y for yes, n for no: ") 
  
  if auction_continue == "n":
    bidding_finished = True 
    find_highest_bidder(auction_dict)
  elif auction_continue == "y":
    clear()

