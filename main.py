import sys

def parse():

    if len(sys.argv) != 3:
        print("Usage: program.exe pathFile1.x pathFile2.y")
        sys.exit(1)

    return sys.argv[1], sys.argv[2]

if __name__ == "__main__":
    input, output = parse()
    print(f"Input: {input}, Output: {output}")