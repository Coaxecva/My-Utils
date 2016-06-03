import sys, os

ref_path = "~/Indel_Analysis/"

SRmapper_path = "~/quang/SRmapper0.1.5/align "
SHRiMp_path = "~/quang/SHRiMP_2_2_3/bin/gmapper-ls  --ignore-qvs -o 1 --strata "


if __name__ == '__main__':
	f = open(sys.argv[1])
	while True:
		read = f.readline()
		if read == '':
			break
		#print(read)
		print(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		#os.system(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		
		print(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		#os.system(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")

		~/quang/SHRiMP_2_2_3/bin/gmapper-ls  --ignore-qvs -o 1 --strata chr1.fq GRCh37_chr1.fasta > chr1.shrimp.sam &
