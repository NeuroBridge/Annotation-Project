#! /usr/bin/env python3

import argparse
import json
import pathlib

parser = argparse.ArgumentParser(
    description="Read file exported from "
    "labelbuddy and print the annotations."
)
parser.add_argument(
    "labelbuddy_exported_file",
    type=str,
    help="path to the file containing the exported documents and annotations.",
)
args = parser.parse_args()

documents_file = pathlib.Path(args.labelbuddy_exported_file)
documents = json.loads(documents_file.read_text("UTF-8"))
doc = documents[0]
for doc_nb, doc in enumerate(documents):
    print(f"Document # {doc_nb}\n")
    for anno_nb, annotation in enumerate(doc["annotations"]):
        highlighted_text = doc["text"][
            annotation["start_char"] : annotation["end_char"]
        ]
        print(f"Annotation # {anno_nb}\nlabel: {annotation['label_name']}")
        print(f"selected text:\n{highlighted_text}\n")
    print(f"{'':-<70}")
