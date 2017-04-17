from utility.core import *

if (__name__ == "__main__") :
	data = list(readNtranslate("./data/train.txt")) + list(readNtranslate("./data/test.txt"))
	p_vals = trainNpredict(data)

	print('train:',p_vals[-1][0],'s','predict:',p_vals[-1][1],'s')
	p_vals.pop()
	p_vals.pop()
	
	threshold = [-8,-4,4,8]		
		
	for i in range(-20,20,2) :
		threshold.append(i / 10)
		
	threshold.sort()
	
	result_label = list(map(getLabel,p_vals,[0] * len(p_vals))) 
	Evaluation(result_label,data[2])
		
	print("ROC:")
	for i in range(len(threshold)):
		result_label = list(map(getLabel,p_vals,[threshold[i]] * len(p_vals))) 
		Evaluation(result_label,data[2],False)