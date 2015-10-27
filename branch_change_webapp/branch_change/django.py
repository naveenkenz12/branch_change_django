import csv
import math
import sys
class Student:
	rno=0
	name=''
	cat=''
	cpi=0.0
	cbr=''
	pbr=''
	options=[]
	index=20
	key=-1
class Program:
	curen=0
	oc=0
	nc=0
	flag=True
	bname=''
	cpimin=-1
class Allot:
	rno=0
	name=''
	cpi=0.0
	cbr=''
	nbr=''
	index=20
	key=-1
mylist=[]
key=0
with open(sys.argv[1], newline='') as csvfile:
	student = csv.reader(csvfile, delimiter=',')
	for row in student:
		#stud.rno=int(row[0])//Remember to match the input and output file
		if (key!=0):
			stud=Student()
			stud.rno=row[2]
			stud.name=row[3]
			stud.cbr=row[4]
			stud.pbr=row[4]
			stud.cpi=float(row[6])
			stud.cat=row[5]
			stud.options=[]
			stud.key=row[0]
			stud.index=20
			for i in range(7,22):
				stud.options.append(row[i])
				#print(stud.options[0])
			mylist.append(stud)
		key+=1
		#print(stud.cbr)
mylist.sort(key=lambda stud: stud.cpi, reverse=True)
programlist=dict()
branches=[]
with open(sys.argv[2], newline='') as csvfile:
	myprogram = csv.reader(csvfile, delimiter=',')
	for row in myprogram:
		program=Program()
		branch=row[0]
		program.oc=int(row[1])
		program.nc=int(row[2])
		program.curen=int(row[2])
		program.bname=branch
		program.cpimin=11
		programlist[branch]=program
		branches.append(branch)
		#print(branch,programlist[branch].oc,programlist[branch].nc,'\n')
#print(programlist['CS B.Tech'].nc)
#print(programlist.keys())
finallist=[]
count=-1
cpi1=-1.0
cpi2=-1.0
stat=0
while(stat<len(mylist)):
	if(mylist[stat].cat=='GE' or mylist[stat].cat=='OBC'):
		if(mylist[stat].cpi<8):
			allot=Allot()
			allot.rno=mylist[stat].rno
			allot.name=mylist[stat].name
			allot.cbr=mylist[stat].pbr
			allot.nbr='Ineligible'
			allot.cpi=mylist[stat].cpi
			allot.key=mylist[stat].key
			finallist.append(allot)
			mylist.remove(mylist[stat])
			stat=stat-1
	elif(mylist[stat].cat=='SC' or mylist[stat].cat=='ST'):
		if(mylist[stat].cpi<7):
			allot=Allot()
			allot.rno=mylist[stat].rno
			allot.name=mylist[stat].name
			allot.cbr=mylist[stat].pbr
			allot.nbr='Ineligible'
			allot.cpi=mylist[stat].cpi
			allot.key=mylist[stat].key
			#allot.index=20
			finallist.append(allot)
			mylist.remove(mylist[stat])
			stat=stat-1
	stat=stat+1
#for i in range(len(mylist)):
	#print(i,mylist[i].rno,mylist[i].name,mylist[i].options[0],mylist[i].index)

#print(len(mylist),'\n')
while (count!=0 and len(mylist)!=0):
	count=0
	i=0
	co=0
	while(co<len(branches)):
		programlist[branches[co]].flag=True
		co=co+1
	while (i<len(mylist)):
		for j in range(0,15):
			#print(j)
			#print(i,mylist[i].options[j],j,mylist[i].rno,mylist[i].cpi,mylist[i].key)
			if (mylist[i].options[j] == ''):
				break
			#if(mylist[i].rno=='15xxxxxx6' and mylist[i].name=='HTA'):
				#print(mylist[i].cbr,programlist[mylist[i].cbr].nc,programlist[mylist[i].options[j]].nc,mylist[i].cbr,mylist[i].options[j],programlist[mylist[i].cbr].oc,programlist[mylist[i].options[j]].oc)
			
			elif (mylist[i].cpi>=9.0 and programlist[mylist[i].options[j]].nc+1<=round(programlist[mylist[i].options[j]].oc*1.1) and mylist[i].index>j and programlist[mylist[i].options[j]].flag==True):
				allot=Allot()
				allot.rno=mylist[i].rno
				allot.name=mylist[i].name
				allot.cbr=mylist[i].pbr
				allot.nbr=mylist[i].options[j]
				mylist[i].cbr=allot.nbr
				allot.cpi=mylist[i].cpi
				allot.key=mylist[i].key
				cpi1=allot.cpi
				flag=True
				for k in range(len(finallist)):
					if (allot.key == finallist[k].key):
						programlist[finallist[k].nbr].nc-=1
						programlist[allot.nbr].nc+=1
						finallist[k].nbr=allot.nbr
						mylist[i].index=j
						flag=False
						break
				if (flag == True):
					programlist[allot.nbr].nc+=1
					programlist[allot.cbr].nc-=1
					finallist.append(allot)
					#print("Yooooo")
					mylist[i].index=j
				choice=mylist[i].options[j]
				count+=1
				temp=i+1
				temp1=-1
				while(temp<len(mylist) and mylist[temp].cpi==cpi1):
					if (mylist[i].options[j] in mylist[temp].options):
						temp1=mylist[temp].options.index(mylist[i].options[j])
						if(temp1<mylist[temp].index):
							allot=Allot()
							allot.rno=mylist[temp].rno
							allot.name=mylist[temp].name
							allot.cbr=mylist[temp].pbr
							allot.nbr=mylist[i].options[j]
							mylist[temp].cbr=allot.nbr
							allot.cpi=mylist[temp].cpi
							allot.key=mylist[temp].key
							flag=True
							for k in range(len(finallist)):
								if (allot.key == finallist[k].key):
									programlist[finallist[k].nbr].nc-=1
									programlist[allot.nbr].nc+=1
									finallist[k].nbr=allot.nbr
									mylist[temp].index=temp1
									flag=False
									break
							if (flag == True):
								programlist[allot.nbr].nc+=1
								programlist[allot.cbr].nc-=1
								finallist.append(allot)
								#print("Yooooo")
								mylist[temp].index=temp1
					
							
							if (temp1 == 0):
								mylist.remove(mylist[temp])
								temp=temp-1
					temp=temp+1
					count+=1
				
				if (j == 0):
					mylist.remove(mylist[i])
					i=i-1										
				break
			elif (mylist[i].cpi<9 and programlist[mylist[i].cbr].nc-1>=math.ceil(programlist[mylist[i].cbr].oc*0.75) and programlist[mylist[i].options[j]].nc+1<=round(programlist[mylist[i].options[j]].oc*1.1) and mylist[i].index>j and programlist[mylist[i].options[j]].flag==True):
				allot=Allot()
				allot.rno=mylist[i].rno
				allot.name=mylist[i].name
				allot.cbr=mylist[i].pbr
				allot.nbr=mylist[i].options[j]
				mylist[i].cbr=allot.nbr
				allot.cpi=mylist[i].cpi
				allot.key=mylist[i].key
				cpi1=allot.cpi
				flag=True
				for k in range(len(finallist)):
					if (allot.key == finallist[k].key):
						programlist[finallist[k].nbr].nc-=1
						programlist[allot.nbr].nc+=1
						finallist[k].nbr=allot.nbr
						mylist[i].index=j
						flag=False
						break
				if (flag == True):
					programlist[allot.nbr].nc+=1
					programlist[allot.cbr].nc-=1
					finallist.append(allot)
					mylist[i].index=j
				count+=1
				
				temp=i+1
				temp1=-1
				choice=mylist[i].options[j]

				while(temp<len(mylist) and mylist[temp].cpi==cpi1):
					if (mylist[i].options[j] in mylist[temp].options):
						
						temp1=mylist[temp].options.index(mylist[i].options[j])
						if(temp1<mylist[temp].index):
							allot=Allot()
							allot.rno=mylist[temp].rno
							allot.name=mylist[temp].name
							allot.cbr=mylist[temp].pbr
							allot.nbr=mylist[i].options[j]
							mylist[temp].cbr=allot.nbr
							allot.cpi=mylist[temp].cpi
							allot.key=mylist[temp].key
							flag=True
							for k in range(len(finallist)):
								if (allot.key == finallist[k].key):
									programlist[finallist[k].nbr].nc-=1
									programlist[allot.nbr].nc+=1
									finallist[k].nbr=allot.nbr
									mylist[temp].index=temp1
									flag=False
									break
							if (flag == True):
								programlist[allot.nbr].nc+=1
								programlist[allot.cbr].nc-=1
								finallist.append(allot)
								#print("Yooooo")
								mylist[temp].index=temp1
				
							count+=1
							if (temp1 == 0):
							    mylist.remove(mylist[temp])
							    temp=temp-1
					temp=temp+1
					count+=1
				
				if (j == 0):
					mylist.remove(mylist[i])
					i=i-1
				
				break
			elif(mylist[i].index>j):
				programlist[mylist[i].options[j]].flag=False
		#print(i,'\n')
		i+=1

#allot.rno='9732'
#allot.name='ygskh'
#allot.cbr='dbbs'x
#allot.nbr='dsjbbvj'
#finallist.append(allot)
#finallist.append(allot)
#print(programlist[branches[14]].flag,'\n')

#for i in range(len(mylist)):
#	print(i,mylist[i].rno,mylist[i].name,mylist[i].options[0],mylist[i].index)
#print(len(mylist),'\n')
fin=0

while(fin<len(mylist)):
	allot=Allot()
	allot.rno=mylist[fin].rno
	allot.name=mylist[fin].name
	allot.cbr=mylist[fin].pbr
	allot.nbr='Branch Unchanged'
	allot.cpi=mylist[fin].cpi
	allot.key=mylist[fin].key
	flag=True
	for k in range(len(finallist)):
		if (allot.key == finallist[k].key):
			flag=False
			break
	if (flag==True):
		finallist.append(allot)
	fin=fin+1
fin=0
prog=''
cpi1=11
while(fin<len(finallist)):
	prog=finallist[fin].nbr
	cpi1=finallist[fin].cpi
	if(prog!='Branch Unchanged' and prog!='Ineligible'):
		if(cpi1<programlist[prog].cpimin):
			programlist[prog].cpimin=cpi1
	fin=fin+1
fin=0
while(fin<len(branches)):
	if(programlist[branches[fin]].cpimin==11):
		programlist[branches[fin]].cpimin='NA'
	fin=fin+1
finallist.sort(key=lambda allot: allot.name, reverse=False)
finallist.sort(key=lambda allot: allot.rno, reverse=False)
with open('output.csv', 'w') as csvfile:
	myallotted = csv.writer(csvfile, delimiter=',')
	for i in range(len(finallist)):
		myallotted.writerow([finallist[i].rno]+[finallist[i].name]+[finallist[i].cbr]+[finallist[i].nbr])
with open('output_stats.csv', 'w') as csvfile:
	myallotted1= csv.writer(csvfile, delimiter=',')
	
	for i in range(len(branches)):
		myallotted1.writerow([programlist[branches[i]].bname]+[programlist[branches[i]].cpimin]+[programlist[branches[i]].oc]+[programlist[branches[i]].curen]+[programlist[branches[i]].nc])
