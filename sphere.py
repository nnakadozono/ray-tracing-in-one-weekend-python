import numpy as np
from hittable import Hittable
import vec3

class Sphere(Hittable):
    def __init__(self, center, radius):
        self.__center = center
        self.__radius = radius

    def hit(self, r, ray_tmin, ray_tmax, rec):
        oc = self.__center - r.origin()
        a = r.direction().length_squared()
        h = vec3.dot(r.direction(), oc)
        c = oc.length_squared() - self.__radius * self.__radius
        discriminant = h * h - a * c
        
        if discriminant < 0:
            return False

        sqrtd = np.sqrt(discriminant)

        # Find the nearest root that lies in the acceptable range.
        root = (h - sqrtd) / a
        if (root <= ray_tmin) or (ray_tmax <= root):
            root = (h + sqrtd) / a
            if (root <= ray_tmin) or (ray_tmax <= root):
                return False
            
        rec.t = root
        rec.p = r.at(rec.t)
        outward_normal = (rec.p - self.__center) / self.__radius
        rec.set_face_normal(r, outward_normal)

        return True


