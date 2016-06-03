# Convert SAM to BAM
# Sort BAM
# index BAM
import sys, os
samtools_path = "/public/apps/samtools/0.1.19/"
result_path = "~/100genomes/aligment/"

with open(sys.argv[1]) as openfileobject:
	for info in openfileobject:
		print(info)
		info = result_path + info
		convert = samtools_path + "samtools view -bS " + info.rstrip() + " > " + os.path.splitext(info)[0] +".bam"
		#print(convert)
		os.system(convert)
		sort = samtools_path + "samtools sort " + os.path.splitext(info)[0] + ".bam " + os.path.splitext(info)[0] +"_sorted"
		#print(sort)
		os.system(sort)
		index = samtools_path + "samtools index " + os.path.splitext(info)[0] + "_sorted.bam " + os.path.splitext(info)[0] + "_sorted.bai"
		#print(index)
		os.system(index)
