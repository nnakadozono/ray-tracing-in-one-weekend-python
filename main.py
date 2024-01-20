import sys
import vec3
import color

def main():
    image_width = 256
    image_height = 256

    print("P3")
    print(f"{image_width} {image_height}")
    print("255")

    for j in range(image_height):
        print(f"\rScanlines remaining: {image_height-j} ", file=sys.stderr, end="", flush=True)
        for i in range(image_width):
            r = float(i) / (image_width - 1)
            g = float(j) / (image_height - 1)
            b = 0

            pixel_color = color.Color(r, g, b)
            color.write_color(pixel_color)
    
    print(f"\rDone.                    ", file=sys.stderr, flush=True)
    

if __name__ == '__main__':
    main()