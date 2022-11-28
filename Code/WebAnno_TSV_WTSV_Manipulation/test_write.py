# A basic WebAnno write example!
#
# MDT

from webanno_tsv import Document, Annotation
from dataclasses import replace

sentences = [
    ['First', 'sentence'],
    ['Second', 'sentence']
]
doc = Document.from_token_lists(sentences)

layer_defs = [('Layer1', ['Field1']), ('Layer2', ['Field2', 'Field3'])]
annotations = [
    Annotation(tokens=doc.tokens[1:2], layer='Layer1', field='Field1', label='ABC'),
    Annotation(tokens=doc.tokens[1:3], layer='Layer2', field='Field3', label='XYZ', label_id=1)
]
doc = replace(doc, annotations=annotations, layer_defs=layer_defs)

print(doc.tsv())
