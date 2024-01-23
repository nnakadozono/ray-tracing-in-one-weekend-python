class Ray:
    def __init__(self, origin, direction):
        self.__orig = origin
        self.__dir = direction

    def origin(self):
        return self.__orig
    
    def direction(self):
        return self.__dir
    
    def at(self, t):
        return self.__orig + t * self.__dir
