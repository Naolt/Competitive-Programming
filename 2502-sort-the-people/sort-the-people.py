class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        count_list = [[] for i in range(max(heights)+1)]

        for idx,height in enumerate(heights):
            count_list[height].append(names[idx])

        res = []

        for name_list in reversed(count_list):
            res.extend(name_list)

        return res

            