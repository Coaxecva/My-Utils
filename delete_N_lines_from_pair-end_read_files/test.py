import sys
fn1, fn2 = sys.argv[1], sys.argv[2]
f1 = open(fn1)
f2 = open(fn2)
f1_1 = open("noN" + fn1, "w")
f2_1 = open("noN" + fn2, "w")

while True:
	info1 = f1.readline()
	read1 = f1.readline()
	opt1 = f1.readline()
	qual1 = f1.readline()
	info2 = f2.readline()
	read2 = f2.readline()
	opt2 = f2.readline()
	qual2 = f2.readline()
	#print info1
	if 'N' not in read1 and 'N' not in read2:
		f1_1.write(info1)
		f1_1.write(read1)
		f1_1.write(opt1)
		f1_1.write(qual1)
		f2_1.write(info2)
		f2_1.write(read2)
		f2_1.write(opt2)
		f2_1.write(qual2)
	if info1 == '':
		break
		
f1_1.close()
f2_1.close()