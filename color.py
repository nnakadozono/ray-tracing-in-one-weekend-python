import vec3

Color = vec3.Vec3
def write_color(pixel_color: Color):
    # Write the translated [0, 255] value of each color component.
    ir = int(255.999 * pixel_color.x())
    ig = int(255.999 * pixel_color.y())
    ib = int(255.999 * pixel_color.z())

    print(f"{ir} {ig} {ib}")