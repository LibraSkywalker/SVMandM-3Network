# SVM and M-3 Network

## 小组成员
蔡万鑫 陈茂棠

## 实验环境：
+ CPU：AMD FX-8320 Eight Core CPU
+ Memory: 16G DDR3-1600Mhz
+ 解释器：Python3.5
+ 第三方库：liblinear(可在http://www.lfd.uci.edu/~gohlke/pythonlibs/#liblinear下载)

## 实验方法：
Problem 1 是直接使用SVM进行分类

Problem 2 是将数据经过random_shuffle后分四块，组合后得到四个基分类器，再用Min Max Modular Network得到最终结果

Problem 3 是利用数据的section层和class层信息，将数据分为16个小类，其中有4个正类，12个负类。正类和负类两两结合得到48个基分类器再通过Min Max Modular Network得到最终结果

## 实验结果：

Accuracy :

+ Problem 1 : 96.49341025776744% (36461/37786)
+ Problem 2 : 96.3108029428889% (36392/37786)
+ Problem 3 : 96.79246281691631% (36574/37786)

F1 :

+ Problem 1 : 0.9263052432372259
+ Problem 2 : 0.9223219762449117
+ Problem 3 : 0.9327861579414375


processing Time :

Problem 1 :
+ train: 15.082964897155762s predict: 4.96967339515686s

Problem 2 :
+ process:0 train: 7.568996906280518s predict: 5.028662919998169s
+ process:1 train: 7.658509016036987s predict: 4.84564471244812s
+ process:2 train: 7.508490085601807s predict: 4.703129768371582s
+ process:3 train: 7.33346962928772s predict: 4.3970863819122314s

Problem 3 :
+ process:0 train: 1.2091596126556396s predict: 5.802767992019653s
+ process:1 train: 2.5358359813690186s predict: 5.5852391719818115s
+ process:2 train: 0.5780766010284424s predict: 5.776264667510986s
+ process:3 train: 2.075774669647217s predict: 5.648247718811035s
+ process:4 train: 4.02153205871582s predict: 5.5587358474731445s
+ process:5 train: 0.48206400871276855s predict: 5.733758926391602s
+ process:6 train: 3.1574182510375977s predict: 5.85877537727356s
+ process:7 train: 0.742598295211792  predict: 5.789766073226929s
+ process:8 train: 1.3216753005981445s predict: 5.996293544769287s
+ process:9 train: 0.519568681716919s predict: 6.136812686920166s
+ process:10 train: 1.0066335201263428s predict: 5.418216705322266s
+ process:11 train: 0.45355987548828125s predict: 5.802267551422119s
+ process:12 train: 1.2211616039276123s predict: 5.294700622558594s
+ process:13 train: 2.1437835693359375s predict: 6.063802480697632s
+ process:14 train: 0.5910787582397461s predict: 5.603741407394409s
+ process:15 train: 1.909252643585205s predict: 5.424217700958252s
+ process:16 train: 3.4854612350463867s predict: 5.47522497177124s
+ process:17 train: 0.2925386428833008s predict: 6.160315036773682s
+ process:18 train: 2.9798941612243652s predict: 5.695253610610962s
+ process:19 train: 0.5870778560638428s predict: 6.416349411010742s
+ process:20 train: 1.0856435298919678s predict: 5.506728649139404s
+ process:21 train: 0.32204198837280273s predict: 5.616743326187134s
+ process:22 train: 0.6770899295806885s predict: 6.386344909667969s
+ process:23 train: 0.3335437774658203s predict: 6.065302610397339s
+ process:24 train: 1.6987247467041016s predict: 5.369710683822632s
+ process:25 train: 3.14591646194458s predict: 6.037799119949341s
+ process:26 train: 0.9466252326965332s predict: 5.492226839065552s
+ process:27 train: 2.703357696533203s predict: 6.461354970932007s
+ process:28 train: 4.079039812088013s predict: 5.437247276306152s
+ process:29 train: 0.7981054782867432s predict: 6.095806121826172s
+ process:30 train: 3.2054238319396973s predict: 5.574265480041504s
+ process:31 train: 1.1126468181610107s predict: 5.875777959823608s
+ process:32 train: 1.4861969947814941s predict: 5.53726053237915s
+ process:33 train: 0.8246099948883057s predict: 6.073802709579468s
+ process:34 train: 1.2901701927185059s predict: 6.3053624629974365s
+ process:35 train: 0.800105094909668s predict: 5.887779235839844s
+ process:36 train: 3.3679730892181396s predict: 5.6322455406188965s
+ process:37 train: 4.27106499671936s predict: 5.116176605224609s
+ process:38 train: 2.447824001312256s predict: 5.602745532989502s
+ process:39 train: 3.7244927883148193s predict: 4.944654941558838s
+ process:40 train: 5.352707862854004s predict: 5.538232326507568s
+ process:41 train: 1.8332414627075195s predict: 5.192250728607178s
+ process:42 train: 4.188054084777832s predict: 5.290729999542236s
+ process:43 train: 1.8863203525543213s predict: 4.451918601989746s
+ process:44 train: 2.597343683242798s predict: 4.928152322769165s
+ process:45 train: 1.64378023147583s predict: 4.355483770370483s
+ process:46 train: 2.249797821044922s predict: 4.832639455795288s
+ process:47 train: 1.6882867813110352s predict: 4.3316309452056885s
