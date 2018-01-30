########## SIMPLEST #######
import regex
regex.search(r'\b(amazing){e<2}\s', 'is life amazing lie ao a')


from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner

# Create sequences to be aligned.
a = Sequence('amazing'.split())
b = Sequence('what a amazing disappointingly bad day'.split())

# Create a vocabulary and encode the sequences.
v = Vocabulary()
aEncoded = v.encodeSequence(a)
bEncoded = v.encodeSequence(b)

# Create a scoring and align the sequences using global aligner.
scoring = SimpleScoring(2, -1)
aligner = GlobalSequenceAligner(scoring, -2)
score, encodeds = aligner.align(aEncoded, bEncoded, backtrace=True)

# Iterate over optimal alignments and print them.
for encoded in encodeds:
    alignment = v.decodeSequenceAlignment(encoded)
    print alignment
    print 'Alignment score:', alignment.score
    print 'Percent identity:', alignment.percentIdentity()
    print


from alignment.sequence import Sequence, GAP_ELEMENT
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, LocalSequenceAligner

large_string = "thelargemanhatanproject is a great project in themanhattincity"
query_string = "manhattan"

# Create sequences to be aligned.
a = Sequence(large_string)
b = Sequence(query_string)

# Create a vocabulary and encode the sequences.
v = Vocabulary()
aEncoded = v.encodeSequence(a)
bEncoded = v.encodeSequence(b)

# Create a scoring and align the sequences using local aligner.
scoring = SimpleScoring(1, -1)
aligner = LocalSequenceAligner(scoring, -1, minScore=5)
score, encodeds = aligner.align(aEncoded, bEncoded, backtrace=True)

# Iterate over optimal alignments and print them.
for encoded in encodeds:
    alignment = v.decodeSequenceAlignment(encoded)

    # Simulate a semi-local alignment.
    if len(filter(lambda e: e != GAP_ELEMENT, alignment.second)) != len(b):
        continue
    if alignment.first[0] == GAP_ELEMENT or alignment.first[-1] == GAP_ELEMENT:
        continue
    if alignment.second[0] == GAP_ELEMENT or alignment.second[-1] == GAP_ELEMENT:
        continue

    print alignment
    print 'Alignment score:', alignment.score
    print 'Percent identity:', alignment.percentIdentity()
    print

# Source: https://stackoverflow.com/questions/17740833/checking-fuzzy-approximate-substring-existing-in-a-longer-string-in-python
