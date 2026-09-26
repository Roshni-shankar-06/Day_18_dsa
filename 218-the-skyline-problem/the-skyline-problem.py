import heapq

class Solution(object):
    def getSkyline(self, buildings):
        # Collect all events: (x, negative_height, right_coordinate) for start, 
        # and (x, height, 0) for end.
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, height, 0))
            
        # Sort events by x coordinate. 
        # If x matches, process larger heights/start events first.
        events.sort()
        
        # Result list and min-heap to act as a max-heap (storing [-height, right])
        res = [[0, 0]]
        hp = [(0, float('inf'))]
        
        for x, neg_h, r in events:
            # Remove buildings from heap that have already ended before current x
            while hp[0][1] <= x:
                heapq.heappop(hp)
                
            # If it's a building start event, add to heap
            if neg_h < 0:
                heapq.heappush(hp, (neg_h, r))
         
