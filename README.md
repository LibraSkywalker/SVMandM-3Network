# SVM and M-3 Network

## 小组成员
蔡万鑫 陈茂棠

## 实验环境：
+ CPU：AMD FX-8320 Eight Core CPU
+ Memory: 16G DDR3-1600Mhz
+ 解释器：Python3.5
+ Jupyter Notebook
+ 第三方库：liblinear(可在http://www.lfd.uci.edu/~gohlke/pythonlibs/#liblinear 下载)

## 实验方法：
Problem 1 是直接使用SVM进行分类

Problem 2 是将数据经过random_shuffle后分四块，组合后得到四个基分类器，再用Min Max Modular Network得到最终结果

Problem 3 是利用数据的section层和class层信息，将数据分为16个小类，其中有4个正类，12个负类。正类和负类两两结合得到48个基分类器再通过Min Max Modular Network得到最终结果

## 实验结果：

实验结果可在SVMandM3-Netwrok.ipynb查看，需安装Jupyter Notebook查看
