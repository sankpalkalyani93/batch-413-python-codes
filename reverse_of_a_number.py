# reverse of a number
num = 1234
rem = 0
reverse = 0

while num > 0:
    rem = num % 10
    print("rem : ", rem)
    reverse = reverse * 10 + rem
    num = num // 10 
    print("num : ", num, " => reverse : ", reverse)
