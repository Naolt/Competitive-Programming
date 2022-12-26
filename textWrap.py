import textwrap

def wrap(string, max_width):
    toList = list(string)
    size = len(toList)
    i = max_width
    while i < size:
        
        toList.insert(i,'\n')
        size += 1
        i+=max_width+1
    
    return "".join(toList)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
