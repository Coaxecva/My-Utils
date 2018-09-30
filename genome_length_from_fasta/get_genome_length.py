import sys, argparse, pysam

def get_args():
    parser = argparse.ArgumentParser(description="example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--fa', type=str, required=True)
    return parser.parse_args()

def main(args):
    for en in pysam.FastxFile(args.fa):
        print(en.name, len(en.sequence))

if __name__ == '__main__':
    sys.exit(main(get_args()))