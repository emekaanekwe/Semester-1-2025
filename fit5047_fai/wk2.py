'''
input the values into the empty spots (0's) in the grid 
such that all sides equal 18:

1,2,3,4,5

[0, 8, 0, 0],
[9, 1, 1, 10],
[0, 0, 7, 0]]

'''

class Search:
    def __init__(self):
        self.array = [
                    [0, 8, 0, 0],
                    [9, 1, 1, 10],
                    [0, 0, 7, 0]]
        self.nums = [1,2,3,4,5]

        
    def brute_force(self):
        if len(self.array) == 0:
            return None
        else:
            for i in self.array:
                total = 0
                count = 0
                for j in i:
                    total += j + self.nums[count]
                    count += 1
                    pass #TODO
                    
                
                    
                    
    def meth_2(self):
        for i in self.array:
            if len(self.array[i]) == 18:
                return True
        return None

        
        