class FastaSeq:
def __init__(self, name, sequence):
    self.name = name
    self.sequence = sequence

def get_seqs(file):
    items = []
    index = 0
    for line in file:
        if line.startswith(">"):
            if index >= 1:
                items.append(aninstance)
            index+=1
            name = line[:-1]
            seq = ''
            aninstance = FastaSeq(name, seq)
        else:
            seq += line[:-1]
            aninstance = FastaSeq(name, seq)
    items.append(aninstance)

    return items

def ReverseComplement3(seq):
    for base in seq:
        if base not in 'ATCGatcg':
            print "Error: NOT a DNA sequence"
            return None
    seq1 = 'ATCGTAGCatcgtagc'
    seq_dict = { seq1[i]:seq1[i+4] for i in range(16) if i < 4 or 8<=i<12 }
    return "".join([seq_dict[base] for base in reversed(seq)])

def main():

	print(ReverseComplement3(seq))

 if __name__ = "main":
 	main()
