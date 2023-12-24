import sys
from PIL import Image
def main():
    if len(sys.argv) != 2:
        print("Usage: py test_src.py <image>")
        return
        
    filename = sys.argv[1]
    print(f"Processing file and doing stuff: {filename}")
    image = Image.open(filename)
    image.show()

if __name__ == '__main__':
    main()
