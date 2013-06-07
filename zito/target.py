import sys


def generator(operation):
    if operation == 'add':
        def f(a, b):
            return a + b
    else:
        def f(a, b):
            return a - b
    return f


add = generator('add')
sub = generator('sub')


def entry_point(argv):
    print add(sub(int(argv[1]), 3), 4)
    return 0


def target(*args):
    return entry_point, None


if __name__ == "__main__":
    entry_point(sys.argv)
