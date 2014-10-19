import sys

fn1, fn2, fn3, number = sys.argv[1], sys.argv[2] , sys.argv[3], sys.argv[4]
f1 = open(fn1) # fastq 1
f2 = open(fn2) # fastq 2
f3 = open(fn3) # sam file
f2_1 = open(fn3 + "new", "w")
n = int(number)

print (number + " reads selected.")

# An empty set.
reads = set()
i = 0
while i<n:
	i = i + 1
	info1 = f1.readline()
	if info1 == '':
		break
	name1 = info1.split(" ")
	reads.add(name1[0][1:])
	#print(name1[0][1:])  
	read1 = f1.readline()
	opt1 = f1.readline()
	qual1 = f1.readline()

	info2 = f2.readline()
	name2 = info2.split(" ")
	reads.add(name2[0][1:])
	#print(name2[0][1:])
	read2 = f2.readline()
	opt2 = f2.readline()
	qual2 = f2.readline()

#print(reads)

while True:
	content3 = f3.readline()

	if content3 == '':
		break

	if content3[0] == '@':
		f2_1.write(content3)

	name3 = content3.split("\t")
	#print(name3[0])
	if name3[0] in reads:
		f2_1.write(content3)
		#print(name3[0])
		#print(content3)

f2_1.close()
print("Done.")

'''
#read1 = f1.readlines()
#read2 = f2.readlines()
sam = f3.readlines()

for line1 in f1:
	id = line1.split(" ")[0][1:]
	for line3 in sam:
		if id == line3.split("\t")[0]:
			print line3
			break
	#f3.seek(0)
'''

'''
while True:
	info3 = f3.readline()
	if info3[0] == '@':
		f2_1.write(info3.strip())
		print(info3.strip())
	else:
		f3.seek(0)
		break		


while True:
	
	#f3 = open(fn3)

	info1 = f1.readline()
	if info1 == '':
		break
	name1 = info1.split(" ")
	print(name1[0][1:])

	read1 = f1.readline()
	opt1 = f1.readline()
	qual1 = f1.readline()
	

	info2 = f2.readline()
	name2 = info2.split(" ")
	print(name2[0][1:])

	read2 = f2.readline()
	opt2 = f2.readline()
	qual2 = f2.readline()

	while True:
		info3 = f3.readline()	
		if info3 == '':
			break
		name3 = info3.split("\t")
		if (name3[0] == name1[0][1:]) or (name3[0] == name2[0][1:]):
			print(info3.strip())

	f3.seek(0)

f2_1.close()
'''