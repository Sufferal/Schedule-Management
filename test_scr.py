import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: py test_src.py <filename>")
        return
        
    filename = sys.argv[1]
    print(f"Processing file and doing stuff: {filename}")

if __name__ == '__main__':
    main()
