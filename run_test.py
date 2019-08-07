from RSSC import run
from Metric import Metric
import os
import numpy as np


def run_test():
    root_dir = "/home/jiangx/Backup/DBCSI_v2/DBCSI_V2_Dataset/TestData/"
    lib_path = "./ProjL1InfPyAPI.so"
    dst_name = "D_1"

    print("Processing %s..." % dst_name)
    # load data
    corr_mat_path = os.path.join(root_dir, dst_name + "_corr.npy")
    gt_array_path = os.path.join(root_dir, dst_name + "_label.npy")
    corr_mat = np.load(corr_mat_path)
    gt_array = np.load(gt_array_path)

    print("Solving optimization problem...")
    pred_label = run(corr_mat, lib_path)
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


if __name__ == '__main__':
    run_test()
