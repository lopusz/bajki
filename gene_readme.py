#!/usr/bin/env python3
import json

FNAMES_TITLES = [("Wojtek_i_Smok_Adas.json", "Wojtek i Smok Adaś"),
                ("Inne_bajki.json", "Inne bajki")]


def process_json(fname):
    n = 0
    with open(fname) as f:
        for line in f:
            n+=1

    with open(fname) as f:
        for i, line in enumerate(f):
            d = json.loads(line)

            s = f"{n-i}. [{d['title']}]({d['url']})"

            if "rating" in d:
                rating=" "
                for _ in d["rating"]:
                    rating +=":star:"
                s += rating

            print(s + "\n")
    print()


def main():
    print("# Bajkowy kącik\n\n\n")
    for fname, title in FNAMES_TITLES:
        print(f"## {title}\n")
        process_json(fname)


if __name__ == "__main__":
    main()

