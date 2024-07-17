'''
string = 'RDDDRR'
'''
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        radiant = deque()
        dire = deque()
        
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        index = len(senate)
        while radiant and dire:
            rad = radiant.popleft()
            dir = dire.popleft()
            #compare rad and dir
            
            if rad<dir:
                radiant.append(index)
                
            else: #dir < rad
                dire.append(index)
                
            index +=1
        
        if radiant: 
            return 'Radiant'
        else: 
            return 'Dire'

solution = Solution()

win = solution.predictPartyVictory('RDD')

print(win)
                
            
            
                
                
                
        
        