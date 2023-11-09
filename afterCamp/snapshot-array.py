class SnapshotArray:

    def __init__(self, length: int):
        self.arr = [[] for i in range(length)] 
        self.snap_count = 0
        
    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_count,val))

    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count-1

    def get(self, index: int, snap_id: int) -> int:
        elemIndex = bisect_right(self.arr[index],(snap_id,inf))
        if not self.arr[index] or self.arr[index][elemIndex-1][0] > snap_id:
            return 0
        return self.arr[index][elemIndex-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)