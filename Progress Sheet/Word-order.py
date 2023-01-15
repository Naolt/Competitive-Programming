# Enter your code here. Read input from STDIN. Print output to STDOUT'
dict = {}

def findValue(value):
    dict[value] = dict.get(value,0)+1
   
number = input()
for i in range(int(number)):
    word = input()
    findValue(word)

print(len(dict))
print(*dict.values())
