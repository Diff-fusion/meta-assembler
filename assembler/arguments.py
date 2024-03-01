import logging
from enum import Enum, auto
from .registers import Register, REGISTERS

logger = logging.getLogger(__name__)

class ArgumentType(Enum):
    Register = 1
    Constant = auto()
    Memory = auto()

class Argument:
    type: ArgumentType
    register: Register
    constant: int
    offset: "Argument"
    #pre_increment: bool
    post_increment: bool

    def as_register(self, register: Register):
        self.type = ArgumentType.Register
        self.register = register

    def as_constant(self, constant: int):
        self.type = ArgumentType.Constant
        self.constant = constant

    def as_memory(self, base: Register, offset: "Argument"):
        self.type = ArgumentType.Memory
        self.register = base
        self.offset = offset

    @classmethod
    def from_str(cls, arg: str):
        self = cls()

        match arg[0]:
            case "D" | "A":
                # TODO: allow other registers
                self.as_register(REGISTERS[arg])
            case "#":
                const = int(arg[1:])
                # TODO: handle HI and LO
                self.as_constant(const)
            case "[": # ]
                arg = arg.strip("[]")
                fallback_offset = 0
                if arg.endswith("++"):
                    self.post_increment = True
                    fallback_offset = 1
                elif arg.endswith("--"):
                    self.post_increment = True
                    fallback_offset = -1
                else:
                    self.post_increment = False
                arg = arg.strip("+-")
                str_base, *str_offset = arg.split("+")
                assert len(str_offset) <= 1
                base = REGISTERS[str_base]
                if not str_offset:
                    str_offset = "#" + str(fallback_offset)
                else:
                    str_offset = str_offset[0]
                offset = cls.from_str(str_offset)
                self.as_memory(base, offset)
            case _:
                print(f"Parsing unknown argument: {arg}")
                exit()

        return self

    def __repr__(self):
        match self.type:
            case ArgumentType.Register:
                return f"Argument(type=Register, value={self.register})"
            case ArgumentType.Constant:
                return f"Argument(type=Constant, value={self.constant})"
            case ArgumentType.Memory:
                return f"Argument(type=Memory, base={self.register}, offset={self.offset})"
            case _:
                return "Unknown argument type"
