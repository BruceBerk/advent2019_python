"""Class IntCode implements the intcode computer"""


class IntCode:
    HALT_OP = 99
    ADD_OP = 1
    MUL_OP = 2
    INPUT_OP = 3
    OUTPUT_OP = 4

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

    def decode_instr(self):
        """Decode the instruction at the current instruction pointer
           Return a list containing the op_code followed by the 3 parameter modes
           Parameter modes are either 0 (position mode - the value is the location of the parameter)
           or 1 (immediate mode - the value IS the parameter)
           Parameter modes are the hundreds, thousands and ten thousands digits, read in reverse"""
        ret_val = []
        instr = self.memory[self.inst_ptr]

        # isolate the opcode - last 2 digits
        op_code = instr % 100
        ret_val.append(op_code)

        # get the 3 parameter modes
        params = instr // 100
        while params > 0:
            last_digit = params % 10
            ret_val.append(last_digit)
            params = params // 10

        while len(ret_val) < 4:
            ret_val.append(0)

        return ret_val

    def add(self, param_modes):
        """Perform an add operation"""
        adder1 = 0
        adder2 = 0

        if param_modes[0] == 0:
            adder1 = self.memory[self.memory[self.inst_ptr + 1]]
        else:
            adder1 = self.memory[self.inst_ptr + 1]

        if param_modes[1] == 0:
            adder2 = self.memory[self.memory[self.inst_ptr + 2]]
        else:
            adder2 = self.memory[self.inst_ptr + 2]

        addr3 = self.memory[self.inst_ptr + 3]
        self.memory[addr3] = adder1 + adder2
        return self.inst_ptr + 4

    def mult(self, param_modes):
        """Perform a multiply operation"""
        addr1 = self.memory[self.inst_ptr + 1]
        addr2 = self.memory[self.inst_ptr + 2]
        addr3 = self.memory[self.inst_ptr + 3]
        self.memory[addr3] = self.memory[addr1] * self.memory[addr2]
        return self.inst_ptr + 4

    def input_op(self, param_modes):
        """Input operation"""
        return self.inst_ptr + 2

    def output_op(self, param_modes):
        """Output operation"""
        return self.inst_ptr + 2

    def run_program(self):
        """Run the program in memory, starting from instruction pointer 0"""
        while self.memory[self.inst_ptr] != self.HALT_OP:
            instr = self.decode_instr()
            if instr[0] == self.ADD_OP:
                self.inst_ptr = self.add(instr[1:])
            elif instr[0] == self.MUL_OP:
                self.inst_ptr = self.mult(instr[1:])
            elif instr[0] == self.INPUT_OP:
                self.inst_ptr = self.input_op(instr[1:])
            elif instr[0] == self.OUTPUT_OP:
                self.inst_ptr = self.output_op(instr[1:])

    def clear_program(self):
        """Clear the memory"""
        self.memory = []
        self.inst_ptr = 0
