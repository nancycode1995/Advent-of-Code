#!/usr/bin/env python3

from abc import ABC, abstractmethod

from advent import solution

class Instruction(ABC):
    @abstractmethod
    def execute(self, cpu):
        """Execute the instruction on the CPU."""
        ...

    @classmethod
    @abstractmethod
    def assemble(cls, string):
        """Attempt to the instruction from a line of source code."""
        ...

    @staticmethod
    def _parse(string):
        opcode, operand_string = string.split(maxsplit=1)
        operands = operand_string.split(", ")
        return opcode, operands

class IncrementInstruction(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, cpu):
        cpu.registers[self.register] += 1

    @classmethod
    def assemble(cls, string):
        opcode, operands = cls._parse(string)
        assert(opcode == "inc")
        return cls(*operands)

    def __str__(self):
        return f"inc {self.register}"

class HalfInstruction(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, cpu):
        cpu.registers[self.register] //= 2

    @classmethod
    def assemble(cls, string):
        opcode, operands = cls._parse(string)
        assert(opcode == "hlf")
        return cls(*operands)

    def __str__(self):
        return f"hlf {self.register}"

class TripleInstruction(Instruction):
    def __init__(self, register):
        self.register = register

    def execute(self, cpu):
        cpu.registers[self.register] *= 3

    @classmethod
    def assemble(cls, string):
        opcode, operands = cls._parse(string)
        assert(opcode == "tpl")
        return cls(*operands)

    def __str__(self):
        return f"tpl {self.register}"

class JumpInstruction(Instruction):
    def __init__(self, offset):
        self.offset = offset

    def execute(self, cpu):
        cpu.pc += self.offset

    @classmethod
    def assemble(cls, string):
        opcode, operands = cls._parse(string)
        assert(opcode == "jmp")
        offset_string, = operands
        return cls(int(offset_string) - 1)

    @property
    def offset_string(self):
        return self.offset if self.offset < 0 else f"+{self.offset + 1}"

    def __str__(self):
        return f"jmp {self.offset_string}"

class JumpIfEvenInstruction(Instruction):
    def __init__(self, register, offset):
        self.register = register
        self.offset = offset

    def execute(self, cpu):
        if cpu.registers[self.register] % 2 == 0:
            cpu.pc += self.offset

    @classmethod
    def assemble(cls, string):
        opcode, operands = cls._parse(string)
        assert(opcode == "jie")
        register, offset_string, = operands
        return cls(register, int(offset_string) - 1)

    @property
    def offset_string(self):
        return self.offset if self.offset < 0 else f"+{self.offset + 1}"

    def __str__(self):
        return f"jie {self.register}, {self.offset_string}"

class JumpIfOneInstruction(Instruction):
    def __init__(self, register, offset):
        self.register = register
        self.offset = offset

    def execute(self, cpu):
        if cpu.registers[self.register] == 1:
            cpu.pc += self.offset

    @classmethod
    def assemble(cls, string):
        opcode, operands = cls._parse(string)
        assert(opcode == "jio")
        register, offset_string, = operands
        return cls(register, int(offset_string) - 1)

    @property
    def offset_string(self):
        return self.offset if self.offset < 0 else f"+{self.offset + 1}"

    def __str__(self):
        return f"jio {self.register}, {self.offset_string}"

def assemble_instruction(string):
    """Attempt to assemble an istruction from a line of source code."""

    print(f"Attempting to assemble instruction: {string}")

    instruction_types = IncrementInstruction, HalfInstruction, TripleInstruction, JumpInstruction, JumpIfEvenInstruction, JumpIfOneInstruction

    def try_assemble(instruction_type):
        """Attempt to assemble an instruction. Return the instruction on success, else return None."""
        try:
            return instruction_type.assemble(string)
        except (AssertionError, ValueError):
            pass

    # Return the first successful attemp at assembly as the instruction
    return next(filter(lambda x: x != None, map(try_assemble, instruction_types)))

def assemble(source_code) -> list:
    """Attempt to assemble a program from source code."""
    return list(map(assemble_instruction, source_code.split("\n")))

class CPU:
    def __init__(self):
        self.initialize()

    def initialize(self):
        self.registers = {"a": 0, "b": 0}
        self.pc = 0

    def execute(self, program: list):
        """Execute a program (list of instructions)."""

        # Run until out of bounds
        while self.pc < len(program):

            # Fetch instruction
            instruction = program[self.pc]
            registers_string = "; ".join(f"{k}={v}" for k, v in self.registers.items())
            print(f"[{registers_string}] {self.pc}: {instruction}")

            # Execute instruction
            instruction.execute(self)

            # Increment program counter normally
            self.pc += 1

        registers_string = "; ".join(f"{k}={v}" for k, v in self.registers.items())
        print(f"[{registers_string}] Program terminates at PC={self.pc}")

@solution("23.txt", "Part 1")
def solve(source_code):
    program = assemble(source_code)
    cpu = CPU()
    print("Executing program...")
    cpu.execute(program)
    return cpu.registers["b"]

@solution("23.txt", "Part 2")
def solve(source_code):
    program = assemble(source_code)
    cpu = CPU()
    cpu.registers["a"] = 1
    print("Executing program...")
    cpu.execute(program)
    return cpu.registers["b"]

