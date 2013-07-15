class Node(object):
    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return (type(self) is type(other) and
                self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not (self == other)

    def compile(self, ctx):
        raise NotImplementedError


class Block(Node):
    """
    a list of statements.
    """
    def __init__(self, statements):
        self.statements = statements

    def compile(self, ctx):
        for statement in self.statements:
            statement.compile(ctx)


class Statement(Node):
    def __init__(self, expr):
        self.expr = expr

    def compile(self, ctx):
        self.expr.compile(ctx)


class Number(Node):
    def __init__(self, value):
        self.value = value

    def compile(self, ctx):
        ctx.emit(bytecode.LOAD_CONSTANT, ctx.create_number(self.value))
