def mainloop(program):
    pass


def parse(program):
    pass


def run(input):
    program = parse(input.read())
    mainloop(program)


if __name__ == "__main__":
    import sys
    run(open(sys.argv[1], 'r'))
