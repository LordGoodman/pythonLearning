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
		for k in range(8):
			next_put=condition_cheack(k,len(lis),lis)
			if next_put:
				lis.append(next_put)
				return cheast_placing(lis)
			else :
				return cheast_placing(lis.pop())
				
		if len(lis)==8:
			return print_cheast(lis)
			
		
def condition_cheack(i,lenght,lis):
		if i not in lis:
			if ((lis[lenght-1]+lenght-1)!=(i+lenght-2)) and (abs(lis[lenght-1]-lenght+1)!=abs(i-lenght+2)):
				if (abs(lis[lenght-1]-lenght+1)!=abs(i-lenght)) and ((lis[lenght-1]+lenght-1)!=(i+lenght)):
					if i !=None :
						return i	

def init_list(lis):
	for k in range(8):
		lis.append(k)
		cheast_placing(lis)
		lis=[]			
		
if __name__ == "__main__":
	lis = []
	init_list(lis)