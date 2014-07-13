import sys
import time
import pysam

print "Version of Pysam: ", pysam.__version__

file = sys.argv[1]
debug = sys.argv[2]
samfile = pysam.Samfile(file)

c = 0
for refs in samfile.references:
	print
	print refs	
	if int(debug) == 1:
		for pileupcolumn in samfile.pileup(refs, 0, samfile.lengths[c]+100):
			print 'coverage at base %s = %s' % (pileupcolumn.pos , pileupcolumn.n)
			for pileupread in pileupcolumn.pileups:
				print '\tbase in read %s = %s' % (pileupread.alignment.qname, pileupread.alignment.seq[pileupread.qpos])
	else:

		aligned = 0
		for pileupcolumn in samfile.pileup(refs, 0, samfile.lengths[c]+100):
			aligned = aligned + 1
		print aligned, samfile.lengths[c], (aligned*1.0/samfile.lengths[c])
	c = c + 1
print "Total ref genomes: ", len(samfile.references)

samfile.close()
