class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def is_hexadecimal(s):
            try:
                int(s, 16)
                return True
            except ValueError:
                return False

        def checkIpv4(address):
            if len(address) != 4:
                return "Neither"
            for val in address:
                if len(val) > 1 and val[0] == "0":
                    return "Neither"
                if not val.isnumeric() or not (0 <= int(val) <= 255):
                    return "Neither"
            return "IPv4"
        def checkIpv6(address):
            if len(address) != 8:
                return "Neither"
            for val in address:
                
                if len(val) > 4 or len(val) == 0:
                    return "Neither"
                for char in val:
                    if not is_hexadecimal(char):
                        return "Neither"
            return "IPv6"
        
        dot = queryIP.find('.')
        colon = queryIP.find(':')

        if 0 >= dot >= colon:
            return "Neither"
        if dot > -1:
            return checkIpv4(queryIP.split('.'))
        elif colon > -1:
            return checkIpv6(queryIP.split(':'))
        
        return "Neither"