def find_max(lst, i=0):
    if i == len(lst) - 1:
        return lst[i]

    max_of_rest = find_max(lst, i + 1)
    return lst[i] if lst[i] > max_of_rest else max_of_rest

inp = input('Enter Number list : ').split()
inp = [int(e) for e in inp]
print("max:", find_max(inp))
