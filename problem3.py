from liblinearutil import *
from functools import reduce
import time, queue
from utility.core import *
from multiprocessing import Pool as ThreadPool

def relabel(name) :
	return name[:2]
		
	
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
	p_labels = pool.map(trainNpredict,data)
	
	pool.close()
	pool.join()
	
	p_labels.sort(key = lambda label:label[test_len])
	for i in range(pos * neg) :
		print(p_labels[i][test_len])
	
	labels = []
	second_labels = []
	for i in range(pos * neg) :
		labels.append(p_labels[i]);
		if (i + 1) % neg == 0 :
			second_labels.append(reduce(seq_min,labels));
			labels = []
		
	result_label = list(reduce(seq_max,second_labels));	
	
	Evaluation(result_label,test_label)