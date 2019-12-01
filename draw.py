import argparse
import random

def main(args):
    names = open(args.input).readlines()
    random.seed(args.seed)
    random.shuffle(names)
    open(args.output, 'w+').write(''.join(names))
    print("Random draw saved at: {}".format(args.output))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Draw random shuffle.')
    parser.add_argument('--input', help='txt file with names', nargs='?',
                        default='names.txt')
    parser.add_argument('--output', help='txt output file', nargs='?',
                        default='shuffle.txt')
    parser.add_argument('--seed', help='random seed', nargs='?',
                        type=int, default=None)
    main(parser.parse_args())
