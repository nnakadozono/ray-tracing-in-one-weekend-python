import hittable

class hisstable_list(hittable):
    def __init__(self, object=None):
        self.add(object)
        self.__objects = []
        
    def clear(self):
        self.__objects = []

    def add(self, object):
        self.__objects.append(object)

    def hit(self, r, ray_tmin, ray_tmax, rec):
        temp_rec = hittable.hit_record()
        hit_anything = False
        closest_so_far = ray_tmax

        for object in self.__objects:
            if object.hit(r, ray_tmin, closest_so_far, temp_rec):
                hit_anything = True
                closest_so_far = temp_rec.t
                rec = temp_rec

        return hit_anything






