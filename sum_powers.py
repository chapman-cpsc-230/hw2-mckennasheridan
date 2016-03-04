user_inputb = input("Enter a positive float")
b = float(user_inputb)
user_inputn = input("Enter a positive integer")
n = int(user_inputn)
i = 0
sum = 0
while i <= n:
    sum = sum + b**i
    i = i+1
print("the sum of %d to %d powers = %d" % (b,n,sum))
print(b**(n+1)/(b-1))
