# cube of a number 
# 2 * 2 * 2 = 8

num = int(input("Enter value for num : "))

i = 1
result = 1
while i <= 3:
    result *= num
    print(result, " when i is ", i)
    i = i + 1

print("Result of cube : ", result)