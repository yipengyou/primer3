import os
os.system("TextToFasta.py cds.txt coding.fasta")
os.system("dna2proteins.py -i coding.fasta -o proteins.fasta")