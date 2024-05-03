from rtweekend import INFINITY

class Interval():
    def __init__(self, min=-INFINITY, max=INFINITY):
        self.min = min
        self.max = max

    def size(self):
        return self.max - self.min
    
    def contains(self, x):
        return self.min <= x and x <= self.max
    
    def surrounds(self, x):
        return self.min < x and x < self.max
    
    @staticmethod
    def empty():
        return Interval(INFINITY, -INFINITY)
    
    @staticmethod
    def universe():
        return Interval(-INFINITY, INFINITY)
