# 1(a) WAP in python to add elements of list.

num=int(input("Enter the length of list: "))
list=[]

for i in range(num):
    num=int(input("Enter a number:"))
    list.append(num)
print(list)

sum=0
for i in list:
    sum+=i
print("Sum of elements of list = :", sum)


# 1(b)Write a Python program to multiply all the items.


product=1
for i in list:
    product*=i
print("product of elements of list = :", product)


# 1(c) Write a Python program to get the largest number from a list.


largest_number = max(list)

print("The largest number in the list is:", largest_number)


# 1(d) Write a Python program to get the smallest number from a list.

smallest_number = min(list)

print("The smallest number in the list is:", smallest_number)