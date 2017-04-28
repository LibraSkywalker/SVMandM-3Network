from utility.core import *
import os
def printfile(label,features,name) :
	print("writing data to",name);
	f = open(name,"w+")	
	for i in range(len(label)) :
		print(label[i],file = f,end=' ')
				
		for key,value in sorted(features[i].items(),key=lambda item:item[0]) :
			print(key,file = f,end='')
			print(":",file = f,end='')
			print(value,file = f,end=' ')
			
		print("",file = f)

if (__name__ == "__main__") :
    
	# Test Set
	'''
	label,features = readNtranslate("./data/test.txt")
	folder = "./GPUdata/Test/"
	printfile(label,features,folder + "test.txt")
    '''
	
	train_label,train_features = read_problem("./data/train.txt")
	raw_label = train_label  
	train_label = list(map(relabel,train_label))	
	
	segment = []
	l = 0
	total = len(train_label)
	for i in range(total) :
		if (i == total - 1 or train_label[i] != train_label[i + 1]) :
			segment.append((l,i,train_label[i]))
			l = i
		
	train_label = list(map(translate,train_label))		
	
	'''
	#Problem 1	
	folder = "./GPUdata/Problem1/"
	printfile(train_label,train_features,folder + "train.txt")

	#Problem 3
	folder = "./GPUdata/Problem3/"
	pos = 4
	neg = 12	
	for i in range(pos) :
		for j in range(neg) :
			li,ri,tmp = segment[i]
			lj,rj,tmp = segment[pos + j]
			index = neg * i + j
			printfile(train_label[li:ri] + train_label[lj:rj],
				train_features[li:ri] + train_features[lj:rj],
				folder + "train" + str(index) +".txt"
			)
	 '''
	#Problem 2
	folder = "./GPUdata/Problem2/"
	train_label,train_features = random_shuffle(raw_label,train_features)
	half = 2

	label = []
	features = []

	length = len(train_label)

	group = 4
	half = group // 2
	group_size = length // group
	pair = half * half

	data = []

	for i in range(group) :
		label.append(train_label[i * group_size : (i + 1) * group_size])        
		features.append(train_features[i * group_size :(i + 1) * group_size])
		
	for i in range(half) :
		for j in range(half) :
			index = i * half + j;    
			data = zip(label[i] + label[j + half],features[i] + features[j + half])   
			new_label,new_features = tuple(zip(*sorted(data,key = lambda item : item[0])))     
			printfile(list(map(translate,new_label)),
				list(new_features),
				folder + "train" + str(index) +".txt"
			)
			


