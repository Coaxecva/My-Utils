import pandas
import po
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
args = parser.parse_args()

df = po.read_csv(args.filename, sep="\t")


correctly_mapped = df.query('(indel_pos - mapped_pos == 21)')
correctly_aligned = pandas.DataFrame([ r for r in correctly_mapped.values if r[2].startswith('22') ], columns=df.keys())
print("\t\ttotal\tmap correctly\tsame with profile")
print(args.filename,"\t",len(df),"\t",len(correctly_mapped),"\t",len(correctly_aligned))

if len(correctly_aligned) > 0:
	correctly_aligned_by_chr = correctly_aligned[['ChrID','non_gap_num','opt_num_1_alignment']].groupby('ChrID', sort=False)
	print(correctly_aligned_by_chr.mean())


## correctly mapped and number of optimal affine-gapped alignment is greater than 1.
correctly_mapped = df.query('(indel_pos - mapped_pos == 21) and (opt_num_1_alignment > 1)')
correctly_aligned = pandas.DataFrame([ r for r in correctly_mapped.values if r[2].startswith('22') ], columns=df.keys())
print("correctly mapped, same w profile and >1 multiple opt alignments")
print(len(correctly_aligned))
if len(correctly_aligned) > 0:
	correctly_aligned_by_chr = correctly_aligned[['ChrID','non_gap_num','opt_num_1_alignment']].groupby('ChrID', sort=False)
	print(correctly_aligned_by_chr.mean())
