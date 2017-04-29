# SVM and M-3 Network

## 小组成员
蔡万鑫 陈茂棠

## 实验环境：
+ CPU：AMD FX-8350 Eight Core CPU
+ Memory: 16G DDR3-1600Mhz
+ GPU: GTX 1080Ti
+ 解释器：Python3.5
+ Jupyter Notebook
+ 第三方库：liblinear(可在http://www.lfd.uci.edu/~gohlke/pythonlibs/#liblinear 下载)
+ 第三方库：liblinear.GPU(https://github.com/aydindemircioglu/LIBLINEAR.gpu)
+ TensorFlow 1.1.0

## 实验方法：
Problem 1 是直接使用SVM进行分类

Problem 2 是将数据经过random_shuffle后分四块，组合后得到四个基分类器，再用Min Max Modular Network得到最终结果

Problem 3 是利用数据的section层和class层信息，将数据分为16个小类，其中有4个正类，12个负类。正类和负类两两结合得到48个基分类器再通过Min Max Modular Network得到最终结果

## 实验结果：

实验结果可在SVM_AND_M-3_Network.ipynb查看，需安装Jupyter Notebook或在GitHub上查看

## GPU Accelarate:

GPU数据需要用relabelforGPU.py生成
GPU加速实验的结果可以在SVM_AND_M-3_Network_GPU.ipynb查看，需安装Jupyter Notebook或在GitHub上查看

## CPU/GPU速度对比
| Task  | GPU | CPU |
|:-----:|:---:|:---:|
| Task1 | 18s | 38s |
| Task2 | 34s | 40s |
| Task3 | 80s | 118s|

需要注意的是liblinear.GPU没有实验predcit函数，所以predict函数还是运行在muticore CPU上的。
train函数是由nvcc编译的，因而没有GPU或按照不同版本的CUDA可能导致无法运行，所以可以clone liblinear.GPU的repo然后自行编译
## Multilayer Preceptron

MLP还可以用libsvm2TFRecord.py将数据转化成TFRecord类型后再用sparseMLP求解，需要有Tensorflow。
