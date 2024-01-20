import math

class Vec3():
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]
    
    def y(self):
        return self.e[1]

    def z(self):
        return self.e[2]

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])
    
    def __getitem__(self, num):
        return self.e[num]
    
    def __iadd__(self, v):
        ''' += '''
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self

    def __imul__(self, t):
        ''' *= '''

        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t):
        ''' /= '''
        self.e *= 1/t
        return self

    def length(self):
        return math.sqrt(self.length_squared())
    
    def length_squared(self):
        return self.e[0]*self.e[0] + self.e[1]*self.e[1] + self.e[2]*self.e[2]

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

    def __add__(self, v):
        return Vec3(self.e[0] + v.e[0], self.e[1] + v.e[1], self.e[2] + v.e[2])

    def __sub__(self, v):
        return Vec3(self.e[0] - v.e[0], self.e[1] - v.e[1], self.e[2] - v.e[2])
    
    def __mul__(self, v):
        if isinstance(v, Vec3):
            ''' self * v '''
            return Vec3(self.e[0] * v.e[0], self.e[1] * v.e[1], self.e[2] * v.e[2])
        elif isinstance(v, (int, float)):
            ''' self * t '''
            return Vec3(self.e[0] * v, self.e[1] * v, self.e[2] * v)
        else:
            return NotImplemented
        
    def __rmul__(self, t):
        ''' t * self '''
        return self.__mul__(t)

    def __truediv__(self, t):
        ''' self / t '''
        return self.__mul__(1/t)

Point3 = Vec3

def dot(u, v):
    return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]

def cross(u, v):
    return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                u.e[2] * v.e[0] - u.e[0] * v.e[2],
                u.e[0] * v.e[1] - u.e[1] * v.e[0])

def unit_vector(v):
    return v / v.length()
