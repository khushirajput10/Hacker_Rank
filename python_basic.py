#1. Print "Hello World!")
print("Hello World!")

#2. The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a=int(input())
b=int(input())
c=a+b
d=a-b
e=a*b
print(c)
print(d)
print(e)

#3. The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  
# // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

a = int(input())
b = int(input())
c=a//b
d=a/b
print(c)
print(d)

# 4. The provided code stub reads and integer, n, from STDIN. For all non-negative
# integers i < n, print i2.
# Example
# n=3
# The list of non-negative integers that are less than n = 3 is [0, 1, 2]. Print the
# square of each number on a separate line.

n = int(input())
for i in range(n):
    i=i*i
    print(i)