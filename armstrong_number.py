# armstrong number
num = int(input("Enter value for num : "))
n = num
rem = 0
armstrong = 0
while num > 0:
    rem = num % 10
    armstrong += rem * rem * rem
    num = num // 10

print("armstrong value : ", armstrong)
if(n == armstrong):
    print(n, " is armstrong number.")
else:
    print(n, " is not armstrong number.")