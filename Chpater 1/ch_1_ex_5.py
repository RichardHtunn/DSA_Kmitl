def vickery_auction():
    user_input = input("Enter All Bid : ")

    try:
        bids = [float(x) for x in user_input.split()]
    except ValueError:
        print("Invalid error")
        return

    if len(bids) < 2:
        print("not enough bidder")
        return
    
    highest_bid = max(bids)

    if bids.count(highest_bid) > 1:
        print("error : have more than one highest bid")
        return
    
    bids_copy = bids.copy()
    bids_copy.remove(highest_bid)
    second_highest_bid = max(bids_copy)

    highest_bid = int(highest_bid) if highest_bid.is_integer() else highest_bid
    second_highest_bid = int(second_highest_bid) if second_highest_bid.is_integer() else second_highest_bid

    print(f"winner bid is {highest_bid} need to pay {second_highest_bid}")

if __name__ == "__main__":
    vickery_auction()
