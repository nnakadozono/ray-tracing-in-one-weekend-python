import sys

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

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)

            print(f"{ir} {ig} {ib}")
    
    print(f"\rDone.                    ", file=sys.stderr, flush=True)
    

if __name__ == '__main__':
    main()