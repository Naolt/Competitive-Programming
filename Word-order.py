# Enter your code here. Read input from STDIN. Print output to STDOUT'
dict = {}

def findValue(value):
    if value not in dict:
        dict[value] = 1
    else:
        dict[value] = dict[value]+1

number = input()
for i in range(int(number)):
    word = input()
    findValue(word)

print(len(dict))
print(*dict.values())
