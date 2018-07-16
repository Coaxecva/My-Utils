#!/usr/bin/env python

import pickle
import sys
import argparse
import numpy as np
from collections import Counter

def get_args():
    parser = argparse.ArgumentParser(description="example", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--min', type=float, required=True)
    parser.add_argument('--max', type=float, required=True)
    parser.add_argument('--delta', type=float, required=True)
    parser.add_argument('--index', type=int, required=True)
    return parser.parse_args()

def main(args):
    bins = np.arange(args.min, args.max + args.delta, args.delta)

    bin_index_count = Counter()

    for line in sys.stdin:
        value = float(line.strip().split()[args.index])
        bin_index = int( value // args.delta )
        bin_index_count[bin_index] += 1

    for bin_index in range(len(bins)):
        print ( bins[bin_index], bin_index_count[bin_index])

if __name__ == '__main__':
    sys.exit(main(get_args()))
    
