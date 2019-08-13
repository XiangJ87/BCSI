import sys

import numpy as np
from BCSI import run

from Metric import Metric

# load data and ground truth
print(sys.argv)
_input_mat = np.load(sys.argv[1])
gt_array = np.load(sys.argv[2])

# define hyper-parameters
lib_path = "./ProjL1InfPyAPI.so"
_lambda = 3e-3
mu = .1
maxIter = 50
errThr = 1e-6

# predict
pred_label = run(_input_mat, lib_path, _lambda, mu, errThr, maxIter)

# evaluate
performance = Metric(pred_label, gt_array)
print("\n*****************Performance************************")
print("------------------Metrics1----------------------------")
print("| TP:  %d" % performance[5])
print("| FP:  %d" % performance[6])
print("| TN:  %d" % performance[7])
print("| FN:  %d" % performance[8])
print("| TPR: %.4f" % performance[9])
print("| FPR: %.4f" % performance[10])
print("|-----------------Metrics2----------------------------")
print("| PRE: %.4f" % performance[0])
print("| REC: %.4f" % performance[1])
print("| F1 : %.4f" % performance[2])
print("| RI : %.4f" % performance[3])
print("| ARI: %.4f" % performance[4])
print("|--------------Categories Number----------------------")
print("| Predict Number: %d" % performance[11])
print("| G-Truth Number: %d" % performance[12])
print("******************************************************\n\n")
