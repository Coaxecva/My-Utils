import sys, os

ref_path = "~/Indel_Analysis/"

SRmapper_path = "~/quang/SRmapper0.1.5/align "
SHRiMp_path = "~/quang/SHRiMP_2_2_3/bin/gmapper-ls  --ignore-qvs -o 1 --strata "
Bowtie2_path = "~/quang/bowtie2-2.0.2/bowtie2-align -x "

if __name__ == '__main__':
	
	f = open(sys.argv[1])
	while True:
		read = f.readline()
		if read == '':
			break
		#print(read)
		print(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		#os.system(SRmapper_path+ref_path+"GRCh37_"+read[:-4]+"-SRmapper { "+read[:-3]+"fastq } "+read[:-4]+".SRmapper.sam &")
		
		print(SHRiMp_path+read.strip()+" "+ref_path+"GRCh37_"+read[:-4]+".fasta > "+read[:-4]+".SHRiMP.sam &")
		#os.system(SHRiMp_path+read.strip()+" "+ref_path+"GRCh37_"+read[:-4]+".fasta > "+read[:-4]+".SHRiMP.sam &")

		print(Bowtie2_path+ref_path+"GRCh37_"+read[:-4]+"-bowtie2 "+read.strip()+" -S "+read[:-4]+".Bowtie2.sam &")
		#os.system(Bowtie2_path+ref_path+"GRCh37_"+read[:-4]+"-bowtie2 "+read+" -S "+read[:-4]+".Bowtie2.sam &")
		
