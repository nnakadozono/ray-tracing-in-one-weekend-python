from hittable import Hittable, HitRecord

class Hittable_list(Hittable):
    def __init__(self, object=None):
        self.__objects = []
        self.add(object)
        
    def clear(self):
        self.__objects = []

    def add(self, object):
        if object is not None:
            self.__objects.append(object)

    def hit(self, r, ray_tmin, ray_tmax, rec):
        temp_rec = HitRecord()
        hit_anything = False
        closest_so_far = ray_tmax

        for object in self.__objects:
            if object.hit(r, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                temp_rec.copy_to(rec)

        return hit_anything






