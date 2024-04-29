import vec3

class hit_record:
    def __init__(self):
        self.p = vec3.Point3()
        self.normal = vec3.Vec3()
        self.t = 0.0
        self.front_face = None

    def set_face_normal(self, r, outward_normal):
        # Sets the hit record normal vector.
        # NOTE: the parameter `outward_normal` is assumed to have unit length.
        front_face = vec3.dot(r.direction(), outward_normal) < 0
        self.normal = outward_normal if front_face else -outward_normal
        
class hittable:
    def hit(self, r, ray_tmin, ray_tmax, rec):
        return None