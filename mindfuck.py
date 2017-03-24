#!/usr/bin/env python

import sys
import getch

def execute(filename):
    """
    Executes the content of the file
    """
    f = open(filename, "r")
    eval(f.read())
    f.close()

def eval(code):
    code     = clean(list(code))
    bracemap = build(code)

    cells, codeptr, cellptr = [0], 0, 0

    while codeptr < len(code):
        command = code[codeptr]

        # increment the data pointer (to point to the next cell to the right).
        if command == ">":
            cellptr += 1
            if cellptr == len(cells): cells.append(0)

        # decrement the data pointer (to point to the next cell to the left).
        if command == "<":
            cellptr = 0 if cellptr <= 0 else cellptr - 1

        # increment (increase by one) the byte at the data pointer.
        if command == "+":
            cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 255 else 0

        # decrement (decrease by one) the byte at the data pointer.
        if command == "-":
            cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > 0 else 255

        # if the byte at the data pointer is zero, then instead of moving the
        # instruction pointer forward to the next command, jump it forward to
        # the command after the matching ] command.
        if command == "[" and cells[cellptr] == 0:
            codeptr = bracemap[codeptr]

        # if the byte at the data pointer is nonzero, then instead of moving
        # the instruction pointer forward to the next command, jump it back
        # to the command after the matching [ command.
        if command == "]" and cells[cellptr] != 0:
            codeptr = bracemap[codeptr]

        # output the byte at the data pointer.
        if command == ".":
            sys.stdout.write(chr(cells[cellptr]))

        # accept one byte of input, storing its value in the byte at the data pointer.
        if command == ",":
            cells[cellptr] = ord(getch.getch())

        codeptr += 1

def clean(code):
    """
    Removes characters other than eight language commands.
    """
    return filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], code)

def build(code):
    bracemap = {}
    tmp_bracestack = []

    for position, command in enumerate(code):
        if command == "[":
            tmp_bracestack.append(position)
        if command == "]":
            start = tmp_bracestack.pop()
            bracemap[start] = position
            bracemap[position] = start
    return bracemap

def main():
    if len(sys.argv) == 2:
        execute(sys.argv[1])
    else:
        print "Usage:", sys.argv[0], "filename"
        sys.exit(1)

if __name__ == "__main__":
    main()
