from replit import clear
from art import Auction_logo
print(Auction_logo)

bids={}
bidding_finnished=False

def find_highest_bidder(bidding_record):
    # bidding_record={"Amit":123,"Bobby":321}
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}.")

while not bidding_finnished:
    name=input("What's your name?: ")
    price=int(input("What is your bid? ₹"))
    bids[name]=price
    should_continue=input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue=="no":
        bidding_finnished=True
        clear()
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear()
    else:
        clear()
        print("Please provide a proper input.")
