class HalixCPU:

    def __init__(self):

        self.registers = {
            "R1":0,
            "R2":0,
            "R3":0,
            "ACC":0
        }

        self.memory = [0]*256
        self.pc = 0
        self.program = []


    def load_program(self, code):

        lines = code.split("\n")

        self.program = []

        for line in lines:
            line = line.strip()

            if line == "":
                continue

            self.program.append(line)

        self.pc = 0

        print("PROGRAM LOADED:", self.program)


    def step(self):

        if self.pc >= len(self.program):
            return "HALT"

        instr = self.program[self.pc]

        print("EXECUTING:", instr)

        parts = instr.split()

        op = parts[0]

        if op == "LOAD":

            reg = parts[1]
            value = int(parts[2])

            self.registers[reg] = value


        elif op == "ADD":

            r1 = parts[1]
            r2 = parts[2]

            self.registers[r1] = self.registers[r1] + self.registers[r2]


        elif op == "STORE":

            reg = parts[1]
            addr = int(parts[2])

            self.memory[addr] = self.registers[reg]


        elif op == "READ":

            addr = int(parts[1])

            self.registers["ACC"] = self.memory[addr]


        elif op == "JMP":

            self.pc = int(parts[1])
            return instr


        self.pc += 1

        print("REGISTERS:", self.registers)

        return instr
