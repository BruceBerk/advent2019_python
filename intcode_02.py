"""
Implements an intcode computer:
Process an array of opcodes
Opcode 1 = add two numbers
Opcode 2 = multiply two numbers
Opcode 99 = Halt program

The add and multiply opcodes are followed by the two memory offsets of the operands,
followed by the memory offset to store the result.

After processing a add or multiply operation, add 4 to the instruction pointer
"""

HALT_OP = 99
ADD_OP = 1
MUL_OP = 2


def run_program(memory):
    """Run the intcode program that is stored in the supplied memory, starting at offset 0"""
    instr_ptr = 0
    while memory[instr_ptr] != HALT_OP:
        if memory[instr_ptr] == ADD_OP:
            addr1 = memory[instr_ptr+1]
            addr2 = memory[instr_ptr+2]
            addr3 = memory[instr_ptr+3]
            memory[addr3] = memory[addr1] + memory[addr2]
        elif memory[instr_ptr] == MUL_OP:
            addr1 = memory[instr_ptr+1]
            addr2 = memory[instr_ptr+2]
            addr3 = memory[instr_ptr+3]
            memory[addr3] = memory[addr1] * memory[addr2]

        instr_ptr += 4

    return memory