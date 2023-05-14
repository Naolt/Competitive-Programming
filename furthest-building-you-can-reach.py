class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        size = len(heights)
        heightList = []
        for i in range(size-1):
            if heights[i] < heights[i+1]:
                heightList.append((heights[i+1]-heights[i],i))
        
        for val,index in heightList:
            # print(val,index,bricks,ladders)
            if len(heap) < ladders:
                heapq.heappush(heap,val)    
            else:
                if bricks > 0:
                    smallest = float('inf') if not heap else heapq.heappop(heap)
                    if min(smallest,val) <= bricks:
                        if smallest < val:
                            heapq.heappush(heap,val)
                            bricks -= smallest
                        else:
                            bricks -= val
                            heapq.heappush(heap,smallest)
                    else:
                        return index
                else:
                    return index
        return len(heights)-1