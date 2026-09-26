import heapq

class Solution(object):
    def getSkyline(self, buildings):
        # Collect all events: (x, negative_height, right_coordinate) for start, 
        # and (x, height, 0) for end.
        events = []
      
