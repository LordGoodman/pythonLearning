def BubbleSort(lis):
	for i in range(len(lis)-1):
		for j in range(len(lis)-i-1) :
			if lis[j]>lis[j+1]:
				lis[j],lis[j+1]=lis[j+1],lis[j]
	print lis
	
if __name__ == "__main__":
	a=[6,5,4,3,2,1]
	BubbleSort(a)