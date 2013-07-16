class Frame(object):
    def __init__(self, bytecode):
        self.stack = [None] * bytecode.max_stackdepth
        self.vars = [None] * len(bytecode.names)
        self.stackpos = 0

    def push(self, value):
        self.stack[self.stackpos] = value
        self.stackpos += 1

    def pop(self):
        stackpos = self.stackpos - 1
        value = self.stack[stackpos]
        self.stackpos = stackpos
        return value


def execute(frame, bc):
    code = bc.code
    pc = 0
    while True:
        c = ord(code[pc])
        arg = ord(code[pc + 1])
        pc += 2


def interpret(source):
    bc = compile_ast(parse(source))
    frame = Frame(bc)
    execute(frame, bc)
    return frame
