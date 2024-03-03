import argparse
import logging
from assembler import Assembler

logger = logging.getLogger(__name__)

def main(args):
    assembly = open(args.input).read()
    asm = Assembler()
    asm.assemble(assembly)
    asm.print_instructions()
    if args.output:
        open(args.output, "wb").write(asm.encoded)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("input", help="Input file")
    args = parser.parse_args()
    main(args)
