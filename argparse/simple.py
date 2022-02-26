import argparse

# python3 ./simple.py a --arg2=b
def demo1():
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1')
    parser.add_argument('--arg2')

    arg = parser.parse_args()
    print(arg)


# python3 ./simple.py parser1 arg1
def demo2():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='here')
    subparser = subparsers.add_parser('parser1')
    subparser.add_argument('parser1_arg')

    arg = parser.parse_args()
    print(arg)

demo2()
