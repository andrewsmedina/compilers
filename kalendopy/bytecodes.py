# name, arguments, stack effect
BYTECODES = [
    ("LOAD_CONST", 1, +1),

    ("LOAD_NAME", 1, +1),
    ("STORE_NAME", 1, 0),

    ("BINARY_ADD", 0, -1),
    ("BINARY_SUB", 0, -1),
    ("BINARY_MUL", 0, -1),
    ("BINARY_DIV", 0, -1),
    ("BINARY_LT", 0, -1),
    ("BINARY_GE", 0, -1),

    ("PRINT_ITEM", 0, -1),

    ("JUMP", 1, 0),
    ("JUMP_IF_FALSE", 1, -1),

    ("DISCARD_TOP", 0, -1),

    ("RETURN_NULL", 0, 0),
]

BYTECODE_NAMES = []
BYTECODE_NUM_ARGS = []
BYTECODE_STACK_EFFECT = []
module = sys.modules[__name__]
for i, (bc_name, num_args, stack_effect) in enumerate(BYTECODES):
    setattr(module, bc_name, i)
    BYTECODE_NAMES.append(bc_name)
    BYTECODE_NUM_ARGS.append(num_args)
    BYTECODE_STACK_EFFECT.append(stack_effect)
del i, bc_name, num_args, stack_effect, module

BINOP_BYTECODE = {
    "+": BINARY_ADD,
    "-": BINARY_SUB,
    "*": BINARY_MUL,
    "/": BINARY_DIV,
    "<": BINARY_LT,
    ">=": BINARY_GE,
}
