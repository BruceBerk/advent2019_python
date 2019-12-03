"""Class IntCode implements the intcode computer"""


class IntCode:
    HALT_OP = 99
    ADD_OP = 1
    MUL_OP = 2

    memory = []
    inst_ptr = 0

    def load_prog_from_file(self, file: str) -> None:
        """Read the program from a data file and convert to a list of ints"""
        with open(file) as inp:
            str_dat = inp.read()

        # convert string data into a list of ints
        prog = str_dat.split(',')
        self.memory = [int(x) for x in prog]

    def load_prog_from_buffer(self, prog) -> None:
        """Fill program memory from a buffer"""
        self.memory = [int(x) for x in prog]

    def peek(self, addr: int) -> int:
        """Return contents of a memory address"""
        return self.memory[addr]

    def poke(self, addr: int, val: int) -> None:
        """Replace a memory location with a new value"""
        self.memory[addr] = val

    def add(self):
        """Perform an add operation"""
        addr1 = self.memory[self.inst_ptr + 1]
        addr2 = self.memory[self.inst_ptr + 2]
        addr3 = self.memory[self.inst_ptr + 3]
        self.memory[addr3] = self.memory[addr1] + self.memory[addr2]
        return self.inst_ptr + 4

    def mult(self):
        """Perform a multiply operation"""
        addr1 = self.memory[self.inst_ptr + 1]
        addr2 = self.memory[self.inst_ptr + 2]
        addr3 = self.memory[self.inst_ptr + 3]
        self.memory[addr3] = self.memory[addr1] * self.memory[addr2]
        return self.inst_ptr + 4

    def run_program(self):
        """Run the program in memory, starting from instruction pointer 0"""
        while self.memory[self.inst_ptr] != self.HALT_OP:
            if self.memory[self.inst_ptr] == self.ADD_OP:
                self.inst_ptr = self.add()
            elif self.memory[self.inst_ptr] == self.MUL_OP:
                self.inst_ptr = self.mult()

    def clear_program(self):
        """Clear the memory"""
        self.memory = []
        self.inst_ptr = 0
