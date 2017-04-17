from liblinearutil import *
from functools import reduce
import time
from utility.core import *
from multiprocessing import Pool as ThreadPool
			
if __name__ == '__main__': 
		
	train_label,train_features = read_problem("./data/train.txt")
	train_label = list(map(relabel,train_label))
	
	test_label,test_features = read_problem("./data/test.txt")
	digit_label = list(map(relabel,test_label))
	test_label = list(map(translate,test_label))
	test_len = len(test_label)
		
	segment = []
	l = 0
	total = len(train_label)
	for i in range(total) :
		if (i == total - 1 or train_label[i] != train_label[i + 1]) :
			segment.append((l,i,train_label[i]))
			l = i
		
	train_label = list(map(translate,train_label))
		
	pos = 4
	neg = 12
		
	data = []
	for i in range(pos) :
		for j in range(neg) :
			li,ri,tmp = segment[i]
			lj,rj,tmp = segment[pos + j]
			index = neg * i + j
			data.append([
				train_label[li:ri] + train_label[lj:rj],
				train_features[li:ri] + train_features[lj:rj],
				test_label,
				test_features,
				index]
			)
		
	pool = ThreadPool(4)
	p_vals = pool.map(trainNpredict,data)

		
	pool.close()
	pool.join()

	p_vals.sort(key = lambda label:label[-2])
		
	for i in range(pos * neg):
		print('process:',i,'train:',p_vals[i][-1][0],'s','predict:',p_vals[i][-1][1],'s')
		p_vals[i].pop()
		p_vals[i].pop()
		
		
	result_label = minmax(pos,neg,p_vals,0)
	Evaluation(result_label,test_label)
		
	threshold = [-8,-4,4,8]		
		
	for i in range(-20,20,2) :
		threshold.append(i / 10)
		
	threshold.sort()
			
	print("ROC:")
	for i in range(len(threshold)):
		result_label = minmax(pos,neg,p_vals,threshold[i])
		Evaluation(result_label,test_label,False)
		
		
