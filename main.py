import argparse
import difflib

try:
    from colorama import init
    init()
except:
    pass

from format import line

def run(a, b, use_color):
    with open(a, encoding="utf-8") as f:
        x = f.readlines()
    with open(b, encoding="utf-8") as f:
        y = f.readlines()

    for l in difflib.ndiff(x, y):
        out = line(l, use_color)
        if out:
            print(out)

p = argparse.ArgumentParser()
p.add_argument("file1")
p.add_argument("file2")
p.add_argument("--no-color", action="store_true")

args = p.parse_args()

try:
run(args.file1, args.file2, not args.no_color)
except FileNotFoundError:
    print("file not found")
