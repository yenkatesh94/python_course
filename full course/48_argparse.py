"""argparse parses and validates options supplied to a command-line program.
This example defines a required name and an optional numeric score.
"""

# Topic 48: Command-line arguments with argparse

import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Show a student's score.")
    parser.add_argument("name", help="student name")
    parser.add_argument("--score", type=float, default=0, help="score from 0 to 100")
    return parser


if __name__ == "__main__":
    # Example terminal command:
    #   python 48_argparse.py Maya --score 92
    # Sample arguments keep this lesson runnable without extra setup.
    args = create_parser().parse_args(["Maya", "--score", "92"])
    print(f"{args.name} scored {args.score:g}.")
