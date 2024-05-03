import sys
import numpy as np
import rtweekend
import vec3
import color
import ray
import hittable
import hittable_list
import sphere

def ray_color(r, world):
    rec = hittable.HitRecord()
    if world.hit(r, 0, rtweekend.INFINITY, rec):
        return 0.5 * (rec.normal + color.Color(1.0, 1.0, 1.0))

    unit_direction = vec3.unit_vector(r.direction())
    a = 0.5 * (unit_direction.y() + 1.0)
    return (1-a) * color.Color(1.0, 1.0, 1.0) + a * color.Color(0.5, 0.7, 1.0)

def main():
    # Image
    aspet_ratio = 16.0 / 9.0
    image_width = 400

    # Calculate the image height, and ensure that it's at least 1.
    image_height = int(image_width / aspet_ratio)
    image_height = 1 if (image_height < 1) else image_height

    # World
    world = hittable_list.Hittable_list()
    world.add(sphere.Sphere(vec3.Point3(0,0,-1), 0.5))
    world.add(sphere.Sphere(vec3.Point3(0,-100.5,-1), 100))    
    
    # Camera
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * float(image_width / image_height)
    camera_center = vec3.Point3(0, 0, 0)

    # Calculate the vectors across the horizontal and down the vertical viewport edges.
    viewport_u = vec3.Vec3(viewport_width, 0, 0)
    viewport_v = vec3.Vec3(0, -viewport_height, 0)

    # Calculate the horizontal and vertical delta vectors from pixel to pixel
    pixel_delta_u = viewport_u / image_width
    pixel_delta_v = viewport_v / image_height

    # Calculate the location of the upper left pixel
    viewport_upper_left = camera_center \
                    - vec3.Vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
    pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

    # Render

    print("P3")
    print(f"{image_width} {image_height}")
    print("255")

    for j in range(image_height):
        print(f"\rScanlines remaining: {image_height-j} ", file=sys.stderr, end="", flush=True)
        for i in range(image_width):
            pixel_center = pixel00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
            ray_direction = pixel_center - camera_center
            r = ray.Ray(camera_center, ray_direction)

            pixel_color = ray_color(r, world)
            color.write_color(pixel_color)
    
    print(f"\rDone.                    ", file=sys.stderr, flush=True)

if __name__ == '__main__':
    main()