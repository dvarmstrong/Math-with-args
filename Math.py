# Practice Creating a class and creating new instances 
# Practice chaining methods
# Practice writing flexible functions that can take varying number of arguments


class Mathdojo :
    def __init__(self):
        self.result = 0

    def add( self, num, *nums):
        self.result += num
        print(nums)
        for  num in (nums):
            self.result += num
        print(self.result)
        return self
        
                
    def subtract( self, num, *nums):
        self.result -= num
        for  num in (nums):
                self.result -= num 
        print(self.result)
        return self



x = Mathdojo()

# x.add(2,1,5,4)
x.subtract(10,3)



