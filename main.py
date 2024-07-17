from art import logo
from os import system, name


print(logo)
all_bidders = False
bidders = []
bid_list = []
name_list = []
while not all_bidders:
	def add_bidder(n, b):
		add_player = {}
		add_player["name"] = n
		add_player["bid"] = b
		bidders.append(add_player)

	name = input("What is your name?: ")
	bid = int(input("what is your bid?: $"))
	others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	add_bidder(n=name, b=bid)
	if others == "no":
		all_bidders = True
		print("All bids are closed.")
	clear()

len_bidders = len(bidders)
for items in range(0, len_bidders):
	bid_list.append(bidders[items]["bid"])
	name_list.append(bidders[items]["name"])

highest_bid = max(bid_list)
position_highest_bid = bid_list.index(highest_bid)
name_winner = name_list[position_highest_bid]

print(f"The winner is {name_winner} with a bid of ${highest_bid}!!")