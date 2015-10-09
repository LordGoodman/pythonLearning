global count
count =0
def print_cheast(lis):
	print("----------------------")
	for i in lis:
		for j in range(8):
			if j==i:
				print '#',#end
			else :
				print '*',
		print("\n")
	print("----------------------")
			
def cheast_placing(lis):
		
			#if len(lis) == 0:
			#	lis.append(k)
			#	cheast_placing(lis)
				
			#else :
		next=condition_cheack(len(lis),lis)#this is the inspiration of this program
		for k in next:
					lis.append(k)
					if len(lis)==8:
						global count
						print_cheast(lis)
					#	print lis
						count +=1
					cheast_placing(lis)
					lis.pop()
			
			
		
		
		
def condition_cheack(lenght,lis):#对角线上也不能有相同
	next=[]#可行解数组
	for i in range(8):
		times=0#times for testing the next level,if get len(lis) times then it work
		if i not in lis:
			for k in range(lenght):
				if ((lis[k]+k)!=(i+lenght)) and (abs(i-lis[k])!=abs(lenght-k)):#this is the most important part in this program
	#the formula abs(i-lis[k])!=abs(lenght-k) make sure that every queen can't find another queen in her diagonal line 
					#if (abs(lis[lenght-1]-lenght+1)!=abs(i-lenght)) and ((lis[lenght-1]+lenght-1)!=(i+lenght)):
						if i !=None :
							times +=1
							if times==len(lis):
							 next.append(i)
								#print next
	return next
						
if __name__ == "__main__":
 lis=[]	
 for i in range(8):
	lis.append(i)
	cheast_placing(lis)
	del lis[:]
print count