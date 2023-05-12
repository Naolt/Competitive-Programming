#User function Template for python3
from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        incoming = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        for i in range(N-1):
            other = self.setOrder(alien_dict[i],alien_dict[i+1],graph)
            if other:
                incoming[other] += 1
        
        for i in range(K):
            if chr(97+i) not in incoming:
                queue.append(chr(97+i))
        
        result = ""
        while queue:
            letter = queue.popleft()
            result += letter
            
            for nbr in graph[letter]:
                incoming[nbr] -= 1
                
                if incoming[nbr] == 0:
                    queue.append(nbr)
                
        return result
        
        
    def setOrder(self,word1,word2,graph):
        size1,size2 = len(word1),len(word2)
        for i in range(min(size2,size1)):
            if word1[i] != word2[i]:
                graph[word1[i]].append(word2[i])
                return word2[i]
        # if word1 == word2[:size1]:
        #     if size2 > size1 and word2[size1] != word1[-1]:
        #         graph[word1[-1]].append(word2[size1])
        #         return word2[size1]
        return None
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends