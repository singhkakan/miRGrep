## miRGrep: A miRNA aligner

miRGrep was developed for the specific case of miRNA-seq. Normally in RNA-seq, reads are aligned to mRNA/whole genomes that are usually much longer in length when compared to the reads. That is, an mRNA may be  1000 bp long, whereas reads are usually 50 - 150 base pairs long. Conventional aligner algorithms were developed for alignment of the above case.

However, in case of miRNA, the reads my be 50 - 150 bp long, and usually contain the end to end sequence of miRNA which are 19 - 26 bp long . If we were to search for a specific miRNA sequence in raw fastq file and count the lines that contain a matching sequence, we could get the total count of that given miRNA in each sample. 

miRGrep uses brute force to obtain the raw counts for each mature miRNA.

##Requirements

> Python 2.6.5 or greater

##Usage

The aligner can be used in a linux environment as follows:

```
./miRGrep.py FASTA FASTQ n > output.txt

```
>FASTA: name of the fasta file for which you want to obtain the counts, with .fa extension

>FASTQ: name of the fastq file with .fastq or .fq extension

>n : number of cores (1 if using a single core)

>output : output filenane of your choice.

## Fasta Format

The code has been texted extensively using fasta files downloaded from miRBase. However, these files have the base 'U' in place of 'T' in the sequence of the miRNA. Therefore, fasta files must be edited to switch the U with T, for the alignment to work correctly.

The code has been tested extensively with the following code. 

```
>mmu-let-7g-5p MIMAT0000121 Mus musculus let-7g-5p
TGAGGTAGTAGTTTGTACAGTT
>mmu-let-7g-3p MIMAT0004519 Mus musculus let-7g-3p
ACTGTACAGGCCACTGCCTTGC
>mmu-let-7i-5p MIMAT0000122 Mus musculus let-7i-5p
TGAGGTAGTAGTTTGTGCTGTT
```

Fasta files from miRBase v22 with the base correction ('U' to 'T') for commonly used species will be made available in the repository

##License and Contact

If you have questions regarding this code, please contact Shruti Kakan at singhkak@usc.edu

License: MIT License