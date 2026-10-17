print("*** multiplication or sum ***")

numOne, numTwo = map(int, input("Enter num1 num2 : ").split())

product = numOne * numTwo



if(product > 1000):
    print(f"The result is {numOne + numTwo}")
else:
    print(f"The result is {product}")