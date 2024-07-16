from collections import deque

class RecentCounter:

    def __init__(self):
        self.data = deque() 

    def ping(self, t: int) -> int:
        #push the new request in queue 
        self.data.append(t)
        
        while t - self.data[0] > 3000:
            self.data.popleft()
            
        return len(self.data)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)