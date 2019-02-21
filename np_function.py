# -*- coding: utf-8 -*-
# run in python2.7

import numpy as np
import sys
import io
from scipy import stats

def loadData(filePath):
    file = io.open(filePath, 'r+', encoding='utf-8')
    lines = file.readlines()
    res = []
    for line in lines:
        res.append(int(line))
    file.close()
    return res

f = sys.argv[1]
data = loadData(f)

d_mean = np.mean(data)
d_mode = stats.mode(data)[0][0]
d_median = np.median(data)
d_var = np.var(data)
d_std = np.std(data)

print("平均值为：%f" % d_mean)
print("众数为：%f" % d_mode) #数据中出现次数最多的数值
print("中位数为：%f" % d_median)
print("方差为：%f" % d_var)
print("标准差为:%f" % d_std)
