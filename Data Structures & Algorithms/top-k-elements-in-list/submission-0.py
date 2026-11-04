import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # O(nlogn) logic since heap size is not limited to k but the entire len of list - n
        # heap = [(-freq, num) for num, freq in count.items()]
        # heapq.heapify(heap)

        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)

        return result
        