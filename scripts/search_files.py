#!/usr/bin/env python

import subprocess
from pathlib import Path

import click


@click.command()
@click.argument('keywords', type=str, nargs=-1, required=True)
@click.option("--path", "-p", type=Path, required=True, help="Path to the root directory of the dataset you wish to search")
@click.option("--output", "-o", type=Path, required=True, help="Path to file in which to store list of files containing keywords.")
def search_files(path, keywords, output):
    """Search recursively for files containing any of KEYWORDS a directory provided by PATH for files
    containing one of the strings provided by KEYWORD option then stores the
    paths to these files in the file specified by OPTION"""

    GREP_FLAGS = "-RilE"

    # connect the key words together in regex syntax
    if len(keywords) > 1:
        search_term = "|".join(keywords)
    else:
        search_term = keywords

    grep_cmd = ["grep", GREP_FLAGS, search_term, path]

    print(f"Searching files in {path} for keywords {keywords}")
    grep_return = subprocess.run(grep_cmd,
                                 check=True,
                                 capture_output=True)

    # simple string response from grep
    grep_string = grep_return.stdout.decode("utf-8")
    grep_output = grep_string.split("\n")[:-1]

    print(f"Saving files to {output}")
    with output.open("w", encoding="utf-8") as fout:
        fout.write(grep_string)
    
    print("Output saved!")


if __name__ == "__main__":
    search_files()
