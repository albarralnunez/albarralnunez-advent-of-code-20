from day_8 import Acc, Code, Executor, Jmp, Nop


def test():
    code = Code(
        instructions=[
            Nop(0, 0),
            Acc(1, 1),
            Jmp(2, 4),
            Acc(3, 3),
            Jmp(4, -3),
            Acc(5, -99),
            Acc(6, 1),
            Jmp(7, -4),
            Acc(8, 6),
        ]
    )
    executor = Executor()
    executor.runner(code)
    assert code.accumulator == 5


def test_2():
    code = Code(
        instructions=[
            Nop(0, 0),
            Acc(1, 1),
            Jmp(2, 4),
            Acc(3, 3),
            Jmp(4, -3),
            Acc(5, -99),
            Acc(6, 1),
            Jmp(7, -4),
            Acc(8, 6),
        ]
    )
    executor = Executor()
    solution = executor.code_fixer(code)
    assert solution == 8
