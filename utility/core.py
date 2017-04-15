import linecache,random, numpy
from functools import reduce
from liblinearutil import *
from multiprocessing import Pool as ThreadPool

def translate(name) :
	if (name[0] == 'A') :
		return 1
	else :
		return -1

def readNtranslate(name) :
	label,features = read_problem(name)
	label = list(map(translate,label))
	return (label,features)	
	
	
def random_shuffle(label,features) :
	length = len(label)
	training_set = [[label[i],features[i]] for i in range(length)]
	random.shuffle(training_set)
	label = [training_set[i][0] for i in range(length)]
	features = [training_set[i][1] for i in range(length)]
	return (label,features)	

def trainNpredict(data):
	model = train(data[0],data[1])
	p_label,p_acc,p_vals = predict(data[2],data[3],model)
	if (len(data) == 5) :
		p_label.append(data[4])
	return p_label

def filter_label(label, features,aimLabel) :
	length = len(label)
	new_label = []
	new_features = []
	for  i in range(length) :
		if (label[i] == aimLabel) :
			new_label.append(label[i])
			new_features.append(features[i])
	return (new_label,new_features)
	
def seq_max(a,b) :
	return map(max,a,b)
	
def seq_min(a,b) :
	return map(min,a,b)

def Evaluation(result_label,test_label) :
	
	total = len(test_label)
	correct = reduce(lambda x,y: x + y, map(lambda x,y : x == y , result_label,test_label))
	
	total_A = reduce(lambda x,y: x + y, map(lambda x,y : y == 1 , result_label,test_label))
	total_B = reduce(lambda x,y: x + y, map(lambda x,y : y == -1 , result_label,test_label))
	
	AtoB = reduce(lambda x,y: x + y, map(lambda x,y : x < y , result_label,test_label))
	BtoA = reduce(lambda x,y: x + y, map(lambda x,y : x > y , result_label,test_label))
	
	print("Accuracy =", correct / total * 100,"% (",correct,"/",total,")")
	print("A->B", AtoB / total_A * 100,"% (",AtoB,"/",total_A,")")
	print("B->A", BtoA / total_B * 100,"% (",BtoA,"/",total_B,")")
	
def parseData(line):
	line = line.split(None, 1)
	if len(line) == 1: line += ['']
	label, features = line
	xi = {}
	for e in features.split():
		ind, val = e.split(":")
		if val != 0:
			xi[int(ind)] = float(val)
	
	return label,xi
	
def read_problem(data_file_name):
	"""
	svm_read_problem(data_file_name, return_scipy=False) -> [y, x], y: list, x: list of dictionary
	svm_read_problem(data_file_name, return_scipy=True)  -> [y, x], y: ndarray, x: csr_matrix

	Read LIBSVM-format data from data_file_name and return labels y
	and data instances x.
	"""
	
	if (__name__ == "utility.core") :
		prob_x = []
		prob_y = []
		row_ptr = [0]
		col_idx = []
		
		print(data_file_name,"is loading.");
		
		cache_data = linecache.getlines(data_file_name)

		print(data_file_name,"has been loaded.");
		print("parsing the data.")
		pool = ThreadPool(8)
		data = pool.map(parseData,cache_data)
		data.sort(key=lambda piece:piece[0])
		pool.close()
		pool.join()
		prob_y,prob_x = tuple(zip(*data))

		print("Data has been parsed.")
		return (list(prob_y), list(prob_x))