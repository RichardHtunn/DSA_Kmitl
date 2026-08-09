# vickrey auction
# take five digits and sort it
def Bubble_Sort(items):
    n = len(items)
    if n > 1:
        for i in range(n-1):
            for j in range(n-1-i):
                if items[j] > items[j+1]:
                    temp = items[j]
                    items[j] = items[j+1]
                    items[j+1] = temp
    return items


# This converts every item into an integer: [5, 10, 20, 5, 16]
user_input = [int(x) for x in input("Enter All Bid : ").split()]
# print(user_input)
n = len(user_input)
if n >= 5:
    sorted_items = Bubble_Sort(user_input)
    # debugging line
    # print(sorted_items)
    highest_bid = sorted_items[-1]
    second__bid = sorted_items[-2]
    if highest_bid == second__bid:
        print("error : have more than one highest bid")
    else:
        print(f"winner bid is {highest_bid} need to pay {second__bid}")
else:
    print("not enough bidder")
