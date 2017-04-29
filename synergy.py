import csv
from itertools import combinations as cn

fp = open('test.csv', 'rb')
fr = csv.reader(fp)
l = list(fr)[2:14]
k = []
for i in range(len(l)):
	for j in range((len(l[i]))):
		if( l[i][j] == ''):
			l[i][j] = 'NaN'


newFp = open('out.csv', 'w+')
newWrite = csv.writer(newFp)
newWrite.writerows(l)
newFp.close()


def skills_syn(p1,p2):
	synk = 0
	for m in xrange(0,len(p1)):
			for n in xrange(0,len(p2)):
				#if (m == 0 and n == 0):
					#synk += (p1[m]+p2[n])*(-0.825)
				if (m == 0 and n == 2):
					synk += (p1[m]+p2[n])*(0.224)
				if (m == 0 and n == 3):
					synk += (p1[m]+p2[n])*(0.071)
				if (m == 0 and n == 4):
					synk += (p1[m]+p2[n])*(0.550)
				#if (m == 0 and n == 5):
					#synk += (p1[m]+p2[n])*(-0.064)
				
				if (m == 1 and n == 1):
					synk += (p1[m]+p2[n])*(0.307)
				#if (m == 1 and n == 2):
					#synk += (p1[m]+p2[n])*(-0.052)
				#if (m == 1 and n == 3):
					#synk += (p1[m]+p2[n])*(-0.134)
				if (m == 1 and n == 4):
					synk += (p1[m]+p2[n])*(0.042)
				#if (m == 1 and n == 5):
					#synk += (p1[m]+p2[n])*(-0.172)

				if (m == 2 and n == 2):
					synk += (p1[m]+p2[n])*(0.293)
				#if (m == 2 and n == 3):
					#synk += (p1[m]+p2[n])*(-0.002)
				#if (m == 2 and n == 4):
					#synk += (p1[m]+p2[n])*(-0.191)
				#if (m == 2 and n == 5):
					#synk += (p1[m]+p2[n])*(-0.132)

				#if (m == 3 and n == 3):
					#synk += (p1[m]+p2[n])*(-0.394)
				if (m == 3 and n == 4):
					synk += (p1[m]+p2[n])*(0.254)
				if (m == 3 and n == 5):
					synk += (p1[m]+p2[n])*(0.128)

				#if (m == 4 and n == 4):
					#synk += (p1[m]+p2[n])*(-0.826)
				#if (m == 4 and n == 5):
					#synk += (p1[m]+p2[n])*(-0.031)

				#if (m == 5 and n == 5):
					#synk += (p1[m]+p2[n])*(-0.284)
	return synk
magicList = []
syn = []
for i in range(12):
	syn.append([])
	for j in range(12):
		syn[i].append(0)
#print syn

for i in xrange(0,len(l)):
	p1 = []
	p1.append(float(l[i][12])/100)
	p1.append(float(l[i][13])/100)
	p1.append(float(l[i][9])/100)
	p1.append(float(l[i][10])/100)
	p1.append(float(l[i][18]))
	p1.append(float(l[i][19]))
	
	for j in xrange(0,len(l)):
		if (i == j):
			continue
		p2 = []
		p2.append(float(l[j][12])/100)
		p2.append(float(l[j][13])/100)
		p2.append(float(l[j][9])/100)
		p2.append(float(l[j][10])/100)
		p2.append(float(l[j][18]))
		p2.append(float(l[j][19]))
		synk = skills_syn(p1,p2)
		syn[i][j] = synk
		syn[j][i] = synk
k = 123
for i in syn:
	for j in i:
		if (j < k):
			k = float(j)

for i in range(len(syn)):
	for j in range(len(syn[i])):
		if (i == j):
			continue
		syn[i][j] += (1+k)
newFp = open('synergyOut.csv', 'w+')
newWrite = csv.writer(newFp)
newWrite.writerows(syn)
