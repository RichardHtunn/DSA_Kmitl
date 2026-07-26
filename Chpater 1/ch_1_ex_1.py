print("*** Rabbit & Turtle ***")
d, Vr, Vt, Vf = map(float, input("Enter Input : ").split())

total_distance = Vf * (d / (Vt - Vr))

print(f"{total_distance:.2f}")