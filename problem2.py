from liblinearutil import *
from functools import reduce
from utility.core import *
from multiprocessing import Pool as ThreadPool

if __name__ == '__main__': 
	label,features = readNtranslate("./data/train.txt")
	test_label,test_features = readNtranslate("./data/test.txt")

	train_label = []
	train_features = []

	length = len(label)

	group = 4
	half = group // 2
	group_size = length // group
	pair = half * half

	data = []
	
	for i in range(group) :
		train_label.append(label[i * group_size : (i + 1) * group_size])
		train_features.append(features[i * group_size :(i + 1) * group_size])
	
	for i in range(half) :
		for j in range(half) :
			
			data.append([train_label[i] + train_label[j + half], 
						train_features[i] + train_features[j + half], 
						test_label,
						test_features])

						
	for i in range(4) :
		print(len(data[i][0]))
	pool = ThreadPool(4)
	p_labels = pool.map(trainNpredict,data)
	
	pool.close()
	pool.join()

	labels = []
	second_labels = []
	for i in range(pair) :
		labels.append(p_labels[i]);
		if (i + 1) % half == 0 :
			second_labels.append(reduce(seq_min,labels));
			labels = []
		
	result_label = list(reduce(seq_max,second_labels));	

	Evaluation(result_label,test_label)


