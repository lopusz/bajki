#!/usr/bin/env python3
import json

print("# Bajkowy kącik\n\n")

with open("bajki.json") as f:
    for line in f:
        d = json.loads(line)
        for k,v in d.items():
            print(f"* [{k}]({v}) \n")

