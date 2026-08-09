'''
 * Group: 26011901
 * 68011339 Hein Htet-San
 * chapter: 1	item: 1	Attempt: 0001
 * Assigned: Monday 6th of July 2026 09:19:40 AM
 *          ==> Submission : Monday 6th of July 2026 12:12:31 PM	
 * Elapsed time: 172 minutes.
 * filename: Rabbit.py
'''
# find the total distance the fly have to go, the moment rabbit catchup the tortoise
print("*** Rabbit & Turtle ***")

user_input = [int(x) for x in input("Enter Input : ").split()]

fspeed = user_input[0]
rspeed = user_input[1]
tspeed = user_input[2]

distance = user_input[3]

catchuptime = distance / (tspeed - rspeed)

flydistance = fspeed * catchuptime

print(f"{flydistance:.2f}")