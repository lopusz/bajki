#!/usr/bin/env python3

import json
import urllib.request
import pathlib

MP3_TARGET_DIR = pathlib.Path("./wojtek_i_smok_adas")
MP3_LIST_FNAME = pathlib.Path("./Wojtek_i_Smok_Adas.json")


def normalize_date(s):
    d, m, y = s.split(".")
    return "-".join([y, m, d])


def normalize_title(s):
    c2c = {
        "ą": "a",
        "ć": "c",
        "ę": "e",
        "ł": "l",
        "ń": "n",
        "ó": "o",
        "ś": "s",
        "ż": "z",
        "ź": "z",
    }

    c_skip = "?!.,;"

    s_res = ""

    for c in s.lower().replace(" ", "-"):
        if c in c_skip:
            continue
        c_res = c2c.get(c, c)
        s_res += c_res
    return s_res


with open(MP3_LIST_FNAME, "rt") as f:

    MP3_TARGET_DIR.mkdir(parents=True)

    for line in f:
        d = json.loads(line)
        url = d["url"]

        date_title = d["title"]
        date = normalize_date(date_title[:10])
        title = normalize_title(date_title[11:])

        fname = date + "-" + title + ".mp3"
        print(f"Downloading {fname}...")
        urllib.request.urlretrieve(url, MP3_TARGET_DIR / fname)
