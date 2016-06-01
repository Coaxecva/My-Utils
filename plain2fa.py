import sys

f = open(sys.argv[1])

i = 0
while True:
	i += 1
	read = f.readline()
	if read == '':
		break
	print(">" + str(i))
	print(read.strip())
