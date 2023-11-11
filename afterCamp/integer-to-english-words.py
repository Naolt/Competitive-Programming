class Solution:
    def numberToWords(self, num: int) -> str:
        number_words = {
            0: "",
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety',
            100: 'Hundred',
            1000: 'Thousand',
            1000000: 'Million',
            1000000000: 'Billion'
        }
        def getWord(number):        
            result = ""
            if len(number) == 3:
                if int(number[0]) != 0:
                    result += number_words[int(number[0])] + " "
                    result += "Hundred "
                if int(number[1]) > 1:
                    result += number_words[int(number[1]+"0")] + " "
                    if int(number[2]) != 0:
                        result += number_words[int(number[2])] + " "
                else:
                    result += number_words[int(number[1:])] + " "
                    return result
            else:
                if len(number) == 2 and int(number[0]) > 1:
                    result += number_words[int(number[0]+"0")] + " "
                    if int(number[1]) != 0:
                        result += number_words[int(number[1])]  + " "
                else:
                    result += number_words[int(number)] + " "
                    return result

            return result

        if num == 0:
            return 'Zero'

        num = str(num)
        arr = [num[max(len(num)-3,0):len(num)]]
        for i in range(len(num)-3,-1,-3):
            if num[max(i-3,0):i]:
                arr.append(num[max(i-3,0):i])

        arr = arr[::-1]
        result = ""
        # print(arr)
        for i in range(0,len(arr)-1):
            power = len(arr)-1-i
            if int(arr[i]):
                result += getWord(arr[i]).strip()
                result += " "
                result += number_words[1000**power]
                result += " "

        result += getWord(arr[-1])

        return result.strip()




        