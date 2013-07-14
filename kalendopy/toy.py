import sys


def main(argv):
    f = open(argv[1])
    data = f.read()
    f.close()
    return 0


if __name__ == '__main__':
    main(sys.argv)
