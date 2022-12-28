"""
 paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
   
   
 dict = {
  (abcd): set(root/a,root/c)
 }
 
 directory 1 = "root/a 1.txt(abcd) 2.txt(efgh)"
 directory 2 = "root/c 3.txt(abcd)"
 directory 3 = "root/c/d 4.txt(efgh)"
 directory 4 = "root 4.txt(efgh)"


"""
from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        pathDict = defaultdict(set)
        for directory in paths:
            fileList = list(directory.split())
            size = len(fileList)
            for i in range(1,size):
                contentIndex = fileList[i].index("(")
                file = fileList[0] + "/" + fileList[i][:contentIndex]
                pathDict[fileList[i][contentIndex-1:len(fileList[i])]].add(file)
        result = []
        for key , value in pathDict.items():
            if len(value) > 1:
                result.append(list(value))
        return result