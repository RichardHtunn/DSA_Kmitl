class Customer:
    def __init__(self, queue, arrival, prep):
        self.queue = queue
        self.arrival = arrival
        self.prep = prep
        self.finish = 0
        self.wait = 0

class CoffeeShop:
    def __init__(self):
        self.b1_free = 0
        self.b2_free = 0
        self.completed_orders = []

    def serve_customer(self, customer):
        if self.b1_free <= self.b2_free:
            start_time = max(customer.arrival, self.b1_free) #the time baristas start working
            customer.wait = start_time - customer.arrival 
            customer.finish = start_time + customer.prep #the time customer got coffee
            self.b1_free = customer.finish #b1's schedule for next person
        else:
            start_time = max(customer.arrival, self.b2_free) 
            customer.wait = start_time - customer.arrival 
            customer.finish = start_time + customer.prep 
            self.b2_free = customer.finish 
        self.completed_orders.append(customer)

print(" ***Cafe***")
User_input = input("Log : ").split("/")
Customer_queue = []
Customer_ID = 1

for i in User_input:
    times = i.split(",")
    arrival = int(times[0])
    prep = int(times[1])
    new_customer = Customer(Customer_ID, arrival, prep)
    Customer_queue.append(new_customer)
    Customer_ID += 1

shop = CoffeeShop()
for j in Customer_queue:
    shop.serve_customer(j)

def sorting_customer(customer):
    return(customer.finish, customer.queue)
shop.completed_orders.sort(key=sorting_customer)

max_wait = 0
longest_wait = -1
for k in shop.completed_orders:
    print(f"Time {k.finish} customer {k.queue} get coffee")
    if k.wait > max_wait:
        max_wait = k.wait
        longest_wait = k.queue

if max_wait == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {longest_wait}")
    print(f"The customer waited for {max_wait} minutes")