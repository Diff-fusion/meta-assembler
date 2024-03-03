import logging
import sys
from assembler import Assembler

logger = logging.getLogger(__name__)

def main():
    assembly = open(sys.argv[1]).read()
    asm = Assembler()
    asm.assemble(assembly)
    asm.print_instructions()


if __name__ == '__main__':
    main()
