# 6(a) Write a Python program to read a four-digit number and find its Sum of digits.

num= int(input("Enter a four digit number:"))
sum=0
while num>0:
    d = num%10
    sum += int(d)
    num = num/10

print("Sum of each digit of inputed number is:",sum)


# 6(b) Write a Python program to read a four-digit number and find reverse of its digit.

num= int(input("Enter a four digit number:"))
rnum=0
while num>0:
    d = num%10
    rnum = rnum * 10 + int(d)
    num = num//10
print("Reverse of inputed number is:",rnum)

