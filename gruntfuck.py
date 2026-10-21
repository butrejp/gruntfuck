#!/usr/bin/env python3
"""gruntfuck"""

import sys

OPS = {
    "hu": ">",
    "hn": "<",
    "uh": "+",
    "hm": "-",
    "ah": ".",
    "eh": ",",
    "ug": "[",
    "mm": "]",
}
def grunt(source):
    return [
        OPS[token.lower()]
        for token in source.split()
        if token.lower() in OPS
    ]
def interpret(source, input_data=""):
    program = grunt(source)
    tape = [0] * 30000
    ptr = 0
    ip = 0
    input_pos = 0
    output = []
    jumps = {}
    stack = []
    for i, op in enumerate(program):
        if op == "[":
            stack.append(i)
        elif op == "]":
            if not stack:
                raise SyntaxError(f"grr {i}")
            start = stack.pop()
            jumps[start] = i
            jumps[i] = start
    if stack:
        raise SyntaxError(f"gra {stack[-1]}")
    while ip < len(program):
        op = program[ip]

        if op == ">":
            ptr += 1
            if ptr >= len(tape):
                tape.append(0)

        elif op == "<":
            ptr -= 1
            if ptr < 0:
                raise IndexError("urgh")

        elif op == "+":
            tape[ptr] = (tape[ptr] + 1) % 256

        elif op == "-":
            tape[ptr] = (tape[ptr] - 1) % 256

        elif op == ".":
            output.append(chr(tape[ptr]))

        elif op == ",":
            if input_pos < len(input_data):
                tape[ptr] = ord(input_data[input_pos]) % 256
                input_pos += 1
            else:
                tape[ptr] = 0

        elif op == "[":
            if tape[ptr] == 0:
                ip = jumps[ip]

        elif op == "]":
            if tape[ptr] != 0:
                ip = jumps[ip]

        ip += 1
    return "".join(output)
if __name__ == "__main__":
    source = sys.stdin.read()
    try:
        print(interpret(source), end="")
    except (SyntaxError, IndexError) as exc:
        print(f"\n[grunt error: {exc}]", file=sys.stderr)
        sys.exit(1)
