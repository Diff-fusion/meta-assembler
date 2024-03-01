import logging
from .arguments import Argument
from .instructions import INSTRUCTIONS
from .instruction_encodings import EncodingType
from .modifiers import parse_modifiers

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def encode_op(op: str, args: list[str]):
    parsed_args = []
    for arg in args:
        parsed_arg = Argument.from_str(arg.strip(","))
        parsed_args.append(parsed_arg)

    for instruction in INSTRUCTIONS:
        if not op.startswith(instruction.name):
            continue
        modifiers = parse_modifiers(op[len(instruction.name):])
        i_args = parsed_args[::-1] if instruction.swap_args else parsed_args
        for encoding in instruction.encodings:
            if encoding.match(i_args, modifiers):
                break
        else:
            logger.debug("Found no encoding for %s in %s, trying other instructions", op, instruction)
            continue
        break
    else:
        print(f"Found no encoding for {op} with args {parsed_args}")
        exit()

    print("Choose encoding", encoding)
    encoded = encoding.encode(i_args, modifiers)
    if encoding.type == EncodingType.Core:
        print(hex(encoded))
    else:
        print(hex(encoded & 0xFFFF), hex(encoded >> 16))

