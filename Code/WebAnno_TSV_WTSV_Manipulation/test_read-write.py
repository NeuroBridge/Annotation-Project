# A basic WebAnno read example!
#
# MDT

from webanno_tsv import webanno_tsv_read_file, Document, Annotation
from dataclasses import replace
from pprint import pprint, pformat

# Read in an Inception Webanno file:

doc = webanno_tsv_read_file('./PMC-markup-extra-short.tsv')

# Now write it again to see diffs

print(doc.tsv())  # To the screen

with open("./testout.tsv", "w") as a_file:
   a_file.write(doc.tsv())

with open("./testout_pretty.txt", "w") as b_file:
   b_file.write(pformat(doc))

# # print(dir(doc))
# # print(doc.layer_defs)

# textfile = open("example.txt", "w")
# a = textfile.write('pythonguides')
# textfile.close()
# # print(len(doc.tokens))

# # print(len(doc.sentence_tokens(doc.sentences[1])))

# # for sentence in doc.sentences:
# #     print(sentence.idx, sentence.text)
