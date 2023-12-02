#!/bin/python3

import argparse
import csv
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--overwrite", action="store_true")
opts = parser.parse_args()

tsv_path = Path.home() / "ProGamer/Writeups/data.tsv"
assert tsv_path.exists()

data = []
with open(tsv_path) as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        n = row["N"]
        key: str = row["Source"]
        youtube = row["YouTube"]

        if not key.startswith("!"):
            continue

        if key.startswith("!AtCoder"):
            pid = key[8:].strip().replace(" ", "")
            contest = pid[:-1].lower()
            url = f"https://atcoder.jp/contests/{contest}/tasks/{contest}_{pid[-1].lower()}"
        elif key.startswith("!CodeForces"):
            pid = key[11:].strip()
            url = f"https://codeforces.com/contest/{pid[:-1]}/problem/{pid[-1]}"
        elif key.startswith("!Kattis"):
            pid = key[7:].strip().lower().replace(" ", "")
            url = f"https://open.kattis.com/problems/{pid}"
        else:
            continue

        key = key[1:]
        contest_name = key.split(" ")[0]

        readme_path = Path(f"{contest_name}/{pid}/README.md")
        if readme_path.exists() and not opts.overwrite:
            print(f"  Already found {readme_path}")
        else:
            with open(readme_path, "w") as f:
                print(f"## {contest_name} {pid}", file=f)
                print("", file=f)
                print(f"Solved in Episode {n}.", file=f)
                print("", file=f)
                print(f"- Problem statement: {url}", file=f)
                if youtube:
                    print(f"- VOD: {youtube}", file=f)
            print(f"* Wrote to {readme_path}")
