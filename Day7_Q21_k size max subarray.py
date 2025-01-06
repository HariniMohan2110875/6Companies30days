import heapq
from collections import deque

class Solution:
    # Function to find maximum of each subarray of size k.
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        maxv = []
        pq = []  # Min-heap to store elements in the current window
        for i in range(n):
            heapq.heappush(pq, arr[i])  # Add current element to the heap

            # Remove the element that is outside the current window
            if i >= k and pq[0] == arr[i - k]:
                pq.pop(0)

            # Once we have reached the window size, we add the max value of the window to maxv
            if i >= k - 1:
                maxv.append(pq[0])

        return maxv
