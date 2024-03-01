import sys
from assembler import encode_op

def main():
    assembly = open(sys.argv[1]).read()

    for line in assembly.splitlines():
        line = line.split("!", 1)[0].strip()
        if not line:
            continue

        op, *args = line.split()
        print(op, args)
        encode_op(op, args)

if __name__ == '__main__':
    main()
