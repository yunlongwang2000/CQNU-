import numpy as np
import pandas as pd
data = pd.read_excel('data.xlsx')
corr = data.corr(method='spearman')
print('相关系数矩阵:\n',np.round(corr,3))
