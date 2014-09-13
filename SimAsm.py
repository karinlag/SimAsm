__author__ = 'karinlag'


from Bio import SeqIO
import os
import sys
import argparse
import random

# TODO need to find sequence that will let me create a sequence
# of numbers that are montonously increasing that will
# give me at scale along which to place my genome for
# N50 calculations


class Genome():
    def __init__(self, seqRecord, mutateRate, scaffoldN50, contigN50):
        self.seqRecord = seqRecord
        self.mutateRate = mutateRate
        self.scaffoldN50 = scaffoldN50
        self.contigN50 = contigN50

    def _mutate(self):
        pass()

    def _scaffoldize(self):
        self._breakGenome(self.scaffoldN50)


    def _contigize(self):
        pass

    def process(self):
        self._mutate()
        self._scaffoldize(
        self._contigize()


def run(infile, outfile):
    pass


if __name__=="__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]


    run(infile, outfile)