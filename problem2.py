from liblinearutil import *
from functools import reduce
from utility.core import *
from multiprocessing import Pool as ThreadPool

if __name__ == '__main__': 
	label,features = readNtranslate("./data/train.txt")
	test_label,test_features = readNtranslate("./data/test.txt")

	label,features = random_shuffle(label,features)
	
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

	pool = ThreadPool(4)
	p_vals = pool.map(trainNpredict,data)
	
	pool.close()
	pool.join()

	for i in range(half * half):
		print('process:',i,'train:',p_vals[i][-1][0],'s','predict:',p_vals[i][-1][1],'s')
		p_vals[i].pop()
		p_vals[i].pop()
	
	result_label = minmax(half,half,p_vals,0)
	Evaluation(result_label,test_label)
	
	threshold = [-8,-4,4,8]		
	for i in range(-20,20,2) :
		threshold.append(i / 10)
	threshold.sort()
			
	print("ROC:")
	for i in range(len(threshold)):
		result_label = minmax(half,half,p_vals,threshold[i])
		Evaluation(result_label,test_label,False)