def swap_case(s):
    result = ""
    for letter in s:
        num = ord(letter)
        
        if num >= 97 and num < 123 :
           
            result += chr(num-32)
        elif num <= 90 and num >= 65:
            result += chr(num+32)
        else:
            result += chr(num)
    
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
