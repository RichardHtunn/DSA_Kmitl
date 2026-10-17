def RANGE(*args):
    if len(args) == 1:
        start, end, step = 0.0, args[0], 1.0
    elif len(args) == 2:
        start, end, step = args[0], args[1], 1.0
    elif len(args) == 3:
        start, end, step = args[0], args[1], args[2]
        
    result = []
    current = start
    if step > 0:
        while current < end:
            result.append(round(current, 3))
            current += step
    elif step < 0:
        while current > end:
            result.append(round(current, 3))
            current += step
            
    return tuple(result)

print('*** New Range ***')
n = [float(i) for i in input('Enter Input : ').split()]
if len(n) == 1:
    print(tuple(RANGE(n[0])))
elif len(n) == 2:
    print(tuple(RANGE(n[0], n[1])))
elif len(n) == 3:
    print(tuple(RANGE(n[0], n[1], n[2])))