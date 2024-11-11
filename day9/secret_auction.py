entries = {}

other_users = "yes"

while other_users == "yes":
    name = input("Enter your name : ")
    bid = int( input("Enter your bid price : "))
    entries[name] = bid
    other_users = input("Are there any other users (yes/no) ? ")
    
    if( other_users == "yes"):
        print('\n' * 50)

max_bidder = ""
max_bid_value = -1

for key, value in entries.items():
    if value > max_bid_value:
        max_bid_value = value
        max_bidder = key

print(f"Max bidder is {max_bidder}")
print(f"Max bid price {max_bid_value}")
