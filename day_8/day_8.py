import re
from copy import copy
from dataclasses import dataclass, field
from functools import reduce
from pathlib import Path
from typing import Callable, List, Type


class InputError(Exception):
    ...


@dataclass(frozen=True)
class Instruction:
    id: int
    value: int

    def execute(self, code: "Code"):
        raise NotImplementedError()


@dataclass(frozen=True)
class Jmp(Instruction):
    def execute(self, code: "Code"):
        code.pointer += self.value


@dataclass(frozen=True)
class Acc(Instruction):
    def execute(self, code: "Code"):
        code.accumulator += self.value
        code.pointer += 1


@dataclass(frozen=True)
class Nop(Instruction):
    def execute(self, code: "Code"):
        code.pointer += 1


def instruction_factory(id: int, instruction_line: str):
    regex = re.match(r"(\w{3}) ([+-]\d*)", instruction_line)
    if not regex:
        raise InputError()
    name, value = regex.group(1), regex.group(2)
    kwargs = {"id": id, "value": int(value)}
    if name == "jmp":
        return Jmp(**kwargs)
    elif name == "acc":
        return Acc(**kwargs)
    elif name == "nop":
        return Nop(**kwargs)


@dataclass
class Code:
    instructions: List[Instruction] = field(repr=False)
    executed_instructions: List[int] = field(default_factory=list, repr=False)
    pointer: int = 0
    accumulator: int = 0
    finished: bool = False

    @classmethod
    def load(cls, code_path: Path):
        with code_path.open() as input:
            instruction = map(
                lambda x: instruction_factory(*x), enumerate(input.read().splitlines())
            )
            return cls(list(instruction))

    def _stop_iteration(self, instruction: Instruction):
        if self.pointer in self.executed_instructions:
            raise StopIteration()
        if instruction.id == len(self.instructions) - 1:
            self.finished = True
            raise StopIteration()

    def __next__(self):
        instruction = copy(self.instructions[self.pointer])
        old_pointer = self.pointer
        instruction.execute(self)
        self._stop_iteration(instruction)
        self.executed_instructions.append(old_pointer)
        return instruction

    def __iter__(self):
        return self


def flip_instruction(
    instructions: List[Instruction], executed_instructions: List[int], flip: int
):
    instruction_to_fix_pointer = executed_instructions[flip]
    instruction_to_fix = instructions[instruction_to_fix_pointer]
    new_instructions = copy(instructions)
    if isinstance(instruction_to_fix, Jmp):
        new_instructions[instruction_to_fix_pointer] = Nop(
            instruction_to_fix.id, instruction_to_fix.value
        )
    elif isinstance(instruction_to_fix, Nop):
        new_instructions[instruction_to_fix_pointer] = Jmp(
            instruction_to_fix.id, instruction_to_fix.value
        )
    return Code(new_instructions)


def code_fixer(code: Code, execution_number: int = 1, debugger_file=None):
    original_instructions = copy(code.instructions)
    flip = -1
    accumulator = runner(code, execution_number, debugger_file)
    executed_instructions = copy(code.executed_instructions)
    while code.finished is False:
        code = flip_instruction(original_instructions, executed_instructions, flip)
        execution_number += 1
        accumulator = runner(code, execution_number, debugger_file)
        flip -= 1
    return accumulator


def runner(code: Code, execution_number: int = 1, debugger_file=None):
    if debugger_file is not None:
        debugger_file.write(f"{'#'*30} - {execution_number} - {'#'*30}\n")
    for instruction in code:
        if debugger_file is not None:
            debugger_file.write(f"{instruction}: {code}\n")
    if debugger_file is not None:
        debugger_file.write(f"{instruction}: {code}\n")
    return code.accumulator


def solver(id: str, input_path_str: str, debug_path_str, executor: Callable):
    input_path = Path(input_path_str)
    code_to_fix = Code.load(input_path)
    debug_path = Path(debug_path_str)
    debug_path.touch()
    with debug_path.open("+w") as debugger_file:
        print(
            f"Solution {id}: {executor(code=code_to_fix, debugger_file=debugger_file)}"
        )


def main():
    solver("test_1", "./input_test.txt", "./solution_test_1.debug", runner)
    solver("1", "./input.txt", "./solution_1.debug", runner)
    solver("test_2", "./input_test.txt", "./solution_test_2.debug", code_fixer)
    solver("2", "./input.txt", "./solution_2.debug", code_fixer)


if __name__ == "__main__":
    main()
