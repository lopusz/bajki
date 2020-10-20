#!/usr/bin/env python3
import json

print("# Bajkowy kącik\n\n\n")

with open("bajki.json") as f:
    for line in f:
        d = json.loads(line)
        print(f"* [{d['title']}]({d['url']})\n")

