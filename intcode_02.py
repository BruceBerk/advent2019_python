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


def run_program(prog):
    """Run the intcode program that is stored in the supplied memory, starting at offset 0"""
    instr_ptr = 0

    # don't change original program
    memory = [x for x in prog]
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


def run_program_with_noun_and_verb(prog, noun, verb):
    """Run intcode program with noun replacing addr 1 and verb replacing addr 2"""
    # don't change original program
    memory = [x for x in prog]
    memory[1] = noun
    memory[2] = verb

    return run_program(memory)
