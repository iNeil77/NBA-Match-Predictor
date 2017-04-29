import os
import csv
import fileinput

#filenName = os.popen('ls | grep playoffs_per_poss').read().splitlines()[0]
#os.rename(filenName, '2.csv')

#filenName = os.popen('ls | grep playoffs_advanced').read().splitlines()[0]
#os.rename(filenName, '4.csv')

filenName = os.popen('ls | grep per_poss').read().splitlines()[0]
os.rename(filenName, '1.csv')

filenName = os.popen('ls | grep advanced').read().splitlines()[0]
os.rename(filenName, '2.csv')

direc = ['1.csv', '2.csv']

fp = []
fr = []
for i in direc:
	fp.append(open(i, 'rb'))

# 1 - per poss, 2-playoff per poss, 3-shootings,4-advanced, 5-playoff advanced, 6-playoff shooting
for i in range(0,len(direc)):
	fr.append(csv.reader(fp[i]))
	#fp[i].close()

new = []

for i in range(0,2):
		l = list(fr[i])
		#k = truncate_table(l)
		k = 0
		for i in range(0,len(l)):
			try:
				#print l[i][0]
				if (l[i][0] == 'Career'):
					k = len(l) - i
					k *= -1
			except:
				#print i
				None
		l = l[1:k]
		new.append(l)

for i in range(0,1):
	if (i == 0):
		for j in new[0]:
			try:
				del j[10]
				del j[12]
				del j[14]
				del j[16]
			except:
				None
	'''if (i == 1):
		for j in new[2]:
			try:
				del j[10]
				del j[12]
				del j[14]
				del j[16]
			except:
				None'''

'''for i in range(0,2):
	for j in range(0, len(new[i])):
		for k in range(0, len(new[i][j])):
			if (new[i][j][k] == ''):
				new[i][j][k] = 'NaN'
				'''


for i in range(0,2):
	f = open(str(i+1)+'.csv', 'w')
	g = csv.writer(f)
	g.writerows(new[i])
	f.close()

for i in direc:
	with open(i, 'r') as file :
	  filedata = file.read()
	filedata = filedata.replace(',,', ',')
	fil = open(i, 'w')
	fil.write(filedata)
	fil.close()
fp = []
fr = []
for i in direc:
	fp.append(open(i, 'rb'))

for i in range(0,len(direc)):
	fr.append(csv.reader(fp[i]))
	

new = []

for i in range(0,2):
		l = list(fr[i])
		#l = l[:-4]
		new.append(l)
		
		#for k in j:
		#	if (k == ''):
		#		j.remove(k)

#print new[1][2][19]

for j in range(0,1):
	#try:
		for i in range(0,len(new[j])):
			#print j, i
			new[j][i].extend(new[j+1][i][5:])
	#except:
		#print j, i

for i in range(0,1):
	for j in range(0,len(new[i][0][5:])):
		new[i][0][j+5] = 'v' + str(j+1)
	
count = 1
for i in new:
	if (count == 2):
		break
	newFp = open('out' + str(count) + '.csv', 'w+')
	newWrite = csv.writer(newFp, delimiter=',')
	newWrite.writerows(i)
	newFp.close()
	count+=1
os.rename('out1.csv', 'regular_out.csv')
os.remove('1.csv')
os.remove('2.csv')
#os.rename('out2.csv', 'playoff_out.csv')