#global and local variables
result = 10

def add(a, b):
    result1 = result + a + b
    return result1

def display():
    x = 100
    print("result : ", result)
    sum = result + x
    print("result after adding x : ", sum)

temp = add(10, 10)
print("Temp : ", temp)

display()
