class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        add: int = numBottles
        
        while(numBottles >= numExchange):
            var: int = numBottles // numExchange 
            add+= var 
            numBottles= numBottles % numExchange + var 
        
        return(add)