# -*- coding: cp936 -*-
'''
矩阵的运算，最终实现奇异值分解SVD
@author slhuang
2014-4-15
'''

import numpy as np
import scipy as sp



if __name__=='__main__':
    M=np.array([[1,1],[2,4],[3,9],[4,16]])
    #print 'M的转置*M is : \n',np.dot(M.T,M)
    #print 'M*M的转置 is ：\n',np.dot(M,M.T)
    print 'M*M的转置 矩阵的特征对为 ：\n',np.linalg.eig(np.dot(M,M.T))
