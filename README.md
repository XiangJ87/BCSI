### BCSI

This is the DEMO of Blind Camera Source Identification. 

***

##### Part1. environment preparation

Our project is implemented on Python3 (>3.5), Ubunut. The packages are listed in `env.txt`. 

To reproduce our python environment, pls run this on terminal:
```bash
cd BCSI
pip install -r env.txt
```

***

##### Part2. run the demo

The DEMO can be run by:
```bash
source activate demo_dbcsi
python run_test.py ./TestingData/S.npy ./TestingData/gt.npy
```
where `./TestingData/S.npy` is the input matrix `S` and `./TestingData/gt.npy` is the ground truth label.

Then the output is like:
```commandline
||Z-C||=7.94e-02, ||C1-C2||=6.27e-04, iteration=0
||Z-C||=1.77e-18, ||C1-C2||=1.66e-04, iteration=1
||Z-C||=1.11e-19, ||C1-C2||=5.08e-05, iteration=2
||Z-C||=3.93e-20, ||C1-C2||=2.93e-05, iteration=3
||Z-C||=3.67e-20, ||C1-C2||=2.10e-05, iteration=4
||Z-C||=1.84e-20, ||C1-C2||=1.61e-05, iteration=5
||Z-C||=2.19e-20, ||C1-C2||=1.39e-05, iteration=6
||Z-C||=2.15e-20, ||C1-C2||=1.16e-05, iteration=7
||Z-C||=1.42e-20, ||C1-C2||=9.82e-06, iteration=8
||Z-C||=1.16e-20, ||C1-C2||=7.13e-06, iteration=9
||Z-C||=9.47e-21, ||C1-C2||=6.69e-06, iteration=10
||Z-C||=8.13e-21, ||C1-C2||=6.47e-06, iteration=11
||Z-C||=7.37e-21, ||C1-C2||=5.96e-06, iteration=12
||Z-C||=2.84e-21, ||C1-C2||=5.01e-06, iteration=13
||Z-C||=3.89e-21, ||C1-C2||=3.19e-06, iteration=14
||Z-C||=1.94e-21, ||C1-C2||=3.04e-06, iteration=15
||Z-C||=2.78e-21, ||C1-C2||=2.92e-06, iteration=16
||Z-C||=3.05e-21, ||C1-C2||=2.18e-06, iteration=17
||Z-C||=0.00e+00, ||C1-C2||=2.14e-06, iteration=18
||Z-C||=1.67e-21, ||C1-C2||=1.95e-06, iteration=19
||Z-C||=4.16e-22, ||C1-C2||=1.10e-06, iteration=20
||Z-C||=2.22e-21, ||C1-C2||=9.82e-07, iteration=21

*****************Performance************************
------------------Metrics1----------------------------
| TP:  5507
| FP:  727
| TN:  24273
| FN:  618
| TPR: 0.8991
| FPR: 0.0291
|-----------------Metrics2----------------------------
| PRE: 0.8834
| REC: 0.8991
| F1 : 0.8912
| RI : 0.9568
| ARI: 0.8642
|--------------Categories Number----------------------
| Predict Number: 5
| G-Truth Number: 5
******************************************************
```
where the first few lines like `||Z-C||=2.19e-20, ||C1-C2||=1.39e-05, iteration=6` is the optimization processing, and the last several lines is the performance of BCSI.

To run the self-generated data, just specific the path of `S` and `gt`, which are the input similarity matrix and ground truth array, respectively. Note that they are saved with `.npy`.  

***

##### Part3. hyper-parameters

There are several parameters in this project:

* `_lambda`: the weight of row-sparsity term. The default setting is `3e-3`.

* `mu`: Lagrangian multiplier. The default setting is `0.1`.

* `maxIter`: The maximum iteration times of optimization. Default to `50`.

* `errThr`: the error threshold to terminate the loop. Default to `1e-6`.

The default values of these parameters can reproduce the results represented in our paper, and they can be modified in `run_test.py`.
***

##### Part4. experimental results in our dataset

We generate 6 dataset with different settings, which can be downloaded in [here](https://url).

This project outperforms the state-of-the-arts, and we present the detail comparison as follow. See Table II-IV.

![Table. 1](https://github.com/XiangJ87/BCSI/blob/master/Figures/TableII-IV.png?raw=true)



###### The detail of Clusters on different dataset.

We compare the results with the **CCC**, whose source code can be found in [here](http://www.grip.unina.it/index.php?option=com_content&view=article&id=79&Itemid=489&jsmallfib=1&dir=JSROOT/Blind_PRNUClustering).

These figures are ploted by Microsoft Excel, where the x-axis is the predicted clusters, y-axis is the image number. Different color denotes the different categories.

Therefore, the best scenario is that each bar is composed by a pure color.

In these figures, the left is the results of **CCC**, and the right is obtained by ours.


![Fig. 1](https://github.com/XiangJ87/BCSI/blob/master/Figures/D1Comparison.png?raw=true)
***
![Fig. 2](https://github.com/XiangJ87/BCSI/blob/master/Figures/D2Comparison.png?raw=true)
***
![Fig. 3](https://github.com/XiangJ87/BCSI/blob/master/Figures/D3Comparison.png?raw=true)
***
![Fig. 4](https://github.com/XiangJ87/BCSI/blob/master/Figures/D4Comparison.png?raw=true)
***
![Fig. 5](https://github.com/XiangJ87/BCSI/blob/master/Figures/D5Comparison.png?raw=true)
***
![Fig. 6](https://github.com/XiangJ87/BCSI/blob/master/Figures/D6Comparison.png?raw=true)

***
