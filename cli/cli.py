#!/bin/python3

import argparse
import algo

parser = argparse.ArgumentParser(
    description="Generate all prime numbers by giving a lower and upper bound"
)

parser.add_argument(
    "--lower",
    type=int,
    help="Lower Bound.Number must be greater than 2.",
)
parser.add_argument(
    "--upper",
    type=int,
    help="Upper Bound.Number must be greater than 2.",
)
parser.add_argument(
    "--algo",
    type=str,
    help="Generation strategy: V1(fast) V2(faster) V3(fastest)",
)

args = parser.parse_args()

upper, lower = args.upper, args.lower

if args.algo == "V1":
    print(algo.algo_V1(lower, upper))
elif args.algo == "V2":
    print(algo.algo_V2(lower, upper))
elif args.algo == "V3":
    print(algo.algo_V3(lower, upper))
else:
    print("Enter V1 or V2 or V3 as input")
