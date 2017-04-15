from utility.core import *

if (__name__ == "__main__") :
	data = list(readNtranslate("./data/train.txt")) + list(readNtranslate("./data/test.txt"))
	result_labels = trainNpredict(data)
	Evaluation(result_labels,data[2])