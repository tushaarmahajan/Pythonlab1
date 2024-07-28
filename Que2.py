# (2) Let A=[‘abc’, ‘xyz’, ‘aba’, 1221’] be a given string, and write a Python
# program that prints the string or strings and their index from the given list,
# ensuring that the first and last characters of the strings to be printed are
# identical.


li = ['abc', 'xyz', 'aba', '1221']

for i in range(len(li)):
    string = li[i]
    if len(string) > 0 and string[0] == string[-1]:
        print(f"String: {string}, Index: {i}")
