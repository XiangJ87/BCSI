import numpy as np
from sklearn.metrics import adjusted_rand_score


def Metric(pred, gt):
    pred_mask = (pred[:, None] == pred) * 2 - 1
    gt_mask = (gt[:, None] == gt) * 2 - 1

    mask = pred_mask - gt_mask

    FN = int(np.sum(mask == -2) / 2)
    FP = int(np.sum(mask == 2) / 2)

    T_mask = pred_mask * (mask == 0)
    TP = int((np.sum(T_mask == 1) - mask.shape[0]) / 2)
    TN = int(np.sum(T_mask == -1) / 2)

    Pre = TP / (TP + FP)
    Rec = TP / (TP + FN)
    F1 = 2 * (Pre * Rec) / (Pre + Rec)
    RI = (TP + TN) / (TP + TN + FP + FN)
    ARI = adjusted_rand_score(gt, pred)
    TPR = TP / (TP + FN)
    FPR = FP / (FP + TN)
    return Pre, Rec, F1, RI, ARI, TP, FP, TN, FN, TPR, \
           FPR, np.unique(pred).size, np.unique(gt).size
