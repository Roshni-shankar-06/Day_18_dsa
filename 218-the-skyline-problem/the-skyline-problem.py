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
      
         
