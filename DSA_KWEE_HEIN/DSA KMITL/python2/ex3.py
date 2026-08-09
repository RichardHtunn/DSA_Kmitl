print('*** New Range ***')

def RANGE(*args):
     # if only one parameter
    result_list = []
    if len(args) == 1:
        start_point = 0
        end_point = args[0]
        # default increasement by one 
        current = start_point
        while current < end_point:
            result_list.append(float(round(current, 2)))
            current += 1
        # debugging line
        # print(result_list)
    elif len(args) == 2:
        start_point = args[0]
        end_point = args[1]
        # result_list.append(start_point)
        # default increasement by one 
        current = start_point
        while current < end_point:
            result_list.append(float(current))
            current += 1
            
     # debugging line
        # print(result_list)
    
    elif len(args) == 3:
        start_point = args[0]
        end_point = args[1]
        difference = args[2]
        # result_list.append(start_point)
        current = start_point
        while current < end_point:
            result_list.append(round(current, 3))
            current += difference
        # debugging line
        # print(result_list)


       
    return result_list


n = [float(i) for i in input('Enter Input : ').split()]
answer = RANGE(*n)


print(tuple(answer))