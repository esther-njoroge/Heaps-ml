
import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  

    def add_num(self, num: int):
        heapq.heappush(self.max_heap, -num)
        if self.max_heap and (-self.max_heap[0]) > (self.min_heap[0] if self.min_heap else float('inf')):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def find_median(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0


medianFinder = MedianFinder()
medianFinder.add_num(1)
medianFinder.add_num(2)
print(medianFinder.find_median())  
medianFinder.add_num(3)
print(medianFinder.find_median()) 