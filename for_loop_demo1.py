# demo for loop + range function
"""for i in range(0, 10+1, 1):
    print(i)"""

"""start = int(input("Enter value for start : "))
stop = int(input("Enter value for stop : "))
step = int(input("Enter value for step : "))

for i in range(start, stop+1, step):
    print("Hello All...! ", i)"""

# print summation of first-n numbers :
"""n = int(input("Enter value for n : "))  # n = 10 -> 1+2+3+4+5+6+7+8+9+10 = 55
sum = 0
for i in range(1, n+1, 1):
    sum += i

print("Summation : ", sum) """

# print table of a given number. Take the number from user.
# num = 5 --> 5 * 1 = 5

"""n=int(input("Enter Value for n:-> "))
for i in range(1,11,1):
    print(n," * ", i, " = ", (i*n))"""

# print the even numbers list till 50. 

# print the factorial of a given number.
# num = 5 => 5*4*3*2*1 = 120 

num = int(input("Enter value for num : "))
fact = 1
for i in range(1, num+1, 1):
    fact *= i

print("Factorial of ", num, " is : ", fact)