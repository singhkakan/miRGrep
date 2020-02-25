#!/usr/bin/python

import sys
import fileinput
from multiprocessing import Process
from itertools import islice

# version with multicore functionality and generator expressions
def files(fasta):
    mir_dict = {}
    fa = open(fasta, 'r')
    miR = fa.readlines()[0::2]
    fa.close
    fa = open(fasta, 'r')
    seq = fa.readlines()[1::2]
    fa.close()
    mir_dict = dict(zip((i.split()[0][1:] for i in miR), (j[1:len(j)-2] for j in seq))) # 1 (removes first base which is 0): len-2 (removes newline and last base)
    return(mir_dict)

def read(fastq):
    read = {}
    with open(fastq, 'r') as handle:
        for lineno, line in enumerate(handle):
            if lineno % 2 != 0:
                if (lineno - 1) % 4 == 0:
                    a_dict = {lineno:line[0:len(line)-1]} #len(line) - 1 removes the newline character
                    read.update(a_dict)
    return(read)

index = files(sys.argv[1])
reads = read(sys.argv[2])

def aligner(index, reads):
    for i in index:
        count = sum((1 for x in reads if index[i] in reads[x]))
        print i, '\t', count, '\t'
    print

def dict_split(d, N):
    it = iter(d)
    for i in xrange(0, len(d), N):
        yield {k:d[k] for k in islice(it, N)}

if __name__ == '__main__':
    worker_pool = []
    N = int(sys.argv[3])
    for item in dict_split(index, len(index)/(N-1)):
        p = Process(target=aligner, args=(item, reads))
        p.start()
        worker_pool.append(p)
    for p in worker_pool:
        p.join()

