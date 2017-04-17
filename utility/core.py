import linecache,random, numpy,time
from functools import reduce
from liblinearutil import *
from multiprocessing import Pool as ThreadPool

def translate(name) :
		if (name[0] == 'A') :
				return 1
		else :
				return -1


def relabel(name) :
		return name[:2]

def getLabel(value,threshold) :		   
	if (value[0] >= threshold) : 
		return 1 
	else :	
		return -1
	
def minmax(outer,inner,p_vals,threshold) :
	labels = []
	second_labels = [] 
	for i in range(outer * inner):
		labels.append(list(map(getLabel,p_vals[i],[threshold] * len(p_vals[i]))))
		if (i + 1) % inner == 0:
			second_labels.append(reduce(seq_min,labels))
			labels = []
	return list(reduce(seq_max,second_labels))

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
		time1=time.time()
		model = train(data[0],data[1])
		time2=time.time()
		p_label,p_acc,p_vals = predict(data[2],data[3],model)
		time3=time.time()
		leng = len(data[2])
		if (len(data) == 5) :
				p_vals.append(data[4])
		p_vals.append([time2 - time1,time3 - time2])
		return p_vals

def filter_label(label, features,aimLabel) :
		length = len(label)
		new_label = []
		new_features = []
		for	 i in range(length) :
				if (label[i] == aimLabel) :
						new_label.append(label[i])
						new_features.append(features[i])
		return (new_label,new_features)
		
def seq_max(a,b) :
		return map(max,a,b)
		
def seq_min(a,b) :
		return map(min,a,b)

def Evaluation(result_label,test_label,verbose = True) :
		total = len(test_label)
		correct = reduce(lambda x,y: x + y, map(lambda x,y : x == y , result_label,test_label))

		tp = reduce(lambda x,y: x + y, map(lambda x,y : x == y and y ==  1, result_label,test_label))
		fn = reduce(lambda x,y: x + y, map(lambda x,y : x < y , result_label,test_label))
		fp = reduce(lambda x,y: x + y, map(lambda x,y : x > y , result_label,test_label))
		tn = reduce(lambda x,y: x + y, map(lambda x,y : x == y and y == -1, result_label,test_label))
		
		if (verbose == True) :
			print("Accuracy =", correct / total * 100,"% (",correct,"/",total,")")

			p = tp / (tp + fp)
			r = tp / (tp + fn)
			f1 = (2 * r * p) / (r + p)
		
			print('F1 =',f1)
		
		else :
			TPR = tp / (tp + fn)
			FPR = fp / (fp + tn)

			print(TPR,'\t',FPR)
		
		
		
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
		svm_read_problem(data_file_name, return_scipy=True)	 -> [y, x], y: ndarray, x: csr_matrix

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
