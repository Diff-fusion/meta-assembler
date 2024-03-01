from dataclasses import dataclass
from .instruction_encodings import *


@dataclass
class Instruction:
    name: str
    encodings: list[Encoding]
    swap_args: bool = False


INSTRUCTIONS = [
    Instruction(
        "ADD",
        [
            # Core GP
            Encoding3ra(0x8000),
            Encoding3rae(0x80000000), # manual seems wrong here
            Encoding2ria(0x8400),
            Encoding2riae(0x84000000, ["T"]),
            Encoding3r(0x0000),
            Encoding3re(0x00000000, ["S"]),
            Encoding2ri(0x0800),
            Encoding2rie(0x08000000, ["S", "T"]),
        ],
    ),
    Instruction(
        "AND",
        [
            # Core GP
            Encoding3r(0x2000),
            Encoding3re(0x20000000, ["S"]),
            Encoding2ri(0x2800, ["M"]),
            Encoding2rie(0x28000000, ["M", "S", "T"]),
        ],
    ),
    Instruction(
        "B",
        [
            # Core GP
            Encoding10i(0x9400),
            Encoding5i(0x9000, ["R"], cc=True),
            Encoding19ie(0x90000000, ["R"], cc=True),
            ]
    ),
    Instruction(
        "CALLR",
        [
            # Core GP
            Encoding1r5i(0x9800),
            Encoding1r19ie(0x98000000),
            ]
    ),
    Instruction(
        "CMP",
        [
            Encoding2rs(0x7000),
            Encoding2rse(0x70000000),
            Encoding1ric(0x7400),
            Encoding1riec(0x74000000),
            Encoding2rso2r(0x7001),
            Encoding2rso2re(0x70010000), # documentation says lsb should be 1
        ]
    ),
    Instruction(
        "GETD",
        [
            Encoding1r3im(0xa800),
            Encoding1r6ime(0xa8003000),
        ]
    ),
    # TODO: MGET, MSET
    Instruction(
        "MOV",
        [
            Encoding2ra(0x8001),
            Encoding2rae(0x80010000), # documentation says lsb shoud be 1
            Encoding1ria(0x8402),
            Encoding1riae(0x84020000),
            Encoding2r(0x0001),
            Encoding2re(0x00010000, ["S"]),
            Encoding1ri(0x0802),
            Encoding1rie(0x08020000, ["S"]),
            # MOV Ux.r,Uy.r: core encoding is madness, only support extended
            Encoding2rcue(0x9c800000),
        ]
    ),
    Instruction(
        "MUL",
        [
        Encoding3r(0x6000),
        Encoding3re(0x60000000),
        Encoding2ri(0x6800),
        Encoding2rie(0x68000000, ["T"]),
        ]
    ),
    Instruction(
        "NEG",
        [
            Encoding2ra(0x8801),
            Encoding2rae(0x88010000), # documentation says lsb shoud be 1
            Encoding1ria(0x8c02),
            Encoding1riae(0x8c020000),
            Encoding2r(0x1001),
            Encoding2re(0x10010000, ["S"]),
            Encoding1ri(0x1802),
            Encoding1rie(0x18020000, ["S"]),
        ]
    ),
    Instruction("NOP", [EncodingN(0x93fe)]),
    Instruction(
        "OR",
        [
            # Core GP
            Encoding3r(0x3000),
            Encoding3re(0x30000000, ["S"]),
            Encoding2ri(0x3800, ["M"]),
            Encoding2rie(0x38000000, ["M", "S", "T"]),
        ],
    ),
    Instruction("RTH", [EncodingN(0x9cef)]),
    Instruction("RTI", [EncodingN(0x9cff)]),
    Instruction(
        "SETD",
        [
            Encoding1r3im(0xa000),
            Encoding1r6ime(0xa0003000),
        ],
        swap_args=True,
    ),
    Instruction(
        "SUB",
        [
            Encoding3ra(0x8800),
            Encoding3rae(0x88000000),
            Encoding2ria(0x8c00),
            Encoding2riae(0x8c000000, ["T"]),
            Encoding3r(0x1000),
            Encoding3re(0x10000000, ["S"]),
            Encoding2ri(0x1800),
            Encoding2rie(0x18000000, ["S", "T"]),
        ]
    ),
    Instruction(
        "SWAP",
        [
            Encoding2rcue(0x9cc00000),
        ]
    ),
]
