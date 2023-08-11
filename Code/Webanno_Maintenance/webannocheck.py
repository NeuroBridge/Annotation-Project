# Webanno Checker
#
# This program checks for specific problems in the Webanno files that
# appear to have been introduced by either Inception or our annotation
# process.
#
# 2023.08.10 - Found *blank* labels in some files; this lists problematic files
#
# MDT

import os
import typer
from typing_extensions import Annotated
from webanno_tsv import webanno_tsv_read_file

def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

def main(
        folder: str,
        human: Annotated[bool, typer.Option(help="Make more human readable")] = False
):
    """Scans a FOLDER of .tsv/.wtsv files and checks for known problems."""
    if human:
        print("Starting Analysis:\n------------------")
    file_list = list_full_paths(folder)
    for file in file_list:
        doc = webanno_tsv_read_file(file)
        for a in doc.annotations:
            if len(a.label) < 2:
                print(file)
                if human:
                    print('   --> Has > 0 empty annotations.')
                break
    if human:
        print("------------------\nEnding Analysis.")

if __name__ == "__main__":
   typer.run(main)
