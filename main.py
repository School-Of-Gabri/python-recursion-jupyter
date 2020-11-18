#! /usr/bin/env python -u

import os
import json

DEBUG = False

def ls(path: str, prefix: str= '') -> dict:
    DEBUG and print(f'{prefix}ls({path})', flush=True)
    struct = {}

    if os.path.isdir(path):
        DEBUG and print(f'{prefix}v', flush=True)
        for branch in os.listdir(path):
            relpath = os.path.join(path, branch)
            if os.path.isfile(relpath):
                continue
            struct[relpath] = ls(relpath, prefix + '  ')

    return struct

if __name__ == "__main__":
    print(json.dumps(ls('..\..')))

