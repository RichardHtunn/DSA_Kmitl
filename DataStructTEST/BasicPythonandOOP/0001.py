print(" *** Wind classification ***")

speed = float(input("Enter wind speed (km/h) : "))

if speed < 0:
    print("!!!Wrong value can't classify.")
elif speed >=0 and speed<= 51.99:
    print("Wind classification is Breeze.")
elif speed >=52.00 and speed <= 55.99:
    print("Wind classification is Depression.")
elif speed >=56.00 and speed <= 101.99:
    print("Wind classification is Tropical Storm.")
elif speed >=102.00 and speed <= 208.99:
    print("Wind classification is Typhoon.")
elif speed >=209.00:
    print("Wind classification is Super Typhoon.")