
n = 5

# 3(b)  to print pyramid pattern.
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
    


# 3(b)  to print right angle triangle.
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print("")

   