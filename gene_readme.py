#!/usr/bin/env python3
import json

print("# Bajkowy kącik\n\n\n")

with open("bajki.json") as f:
    for line in f:
        d = json.loads(line)

        s = f"1. [{d['title']}]({d['url']})"

        if "rating" in d:
            rating=" "
            for _ in d["rating"]:
                rating +=":star:"
            s += rating

        print(s + "\n")


