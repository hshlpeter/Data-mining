# -*- coding: cp936 -*-
'''
��������㣬����ʵ������ֵ�ֽ�SVD
@author slhuang
2014-4-15
'''

import numpy as np
import scipy as sp



if __name__=='__main__':
    M=np.array([[1,1],[2,4],[3,9],[4,16]])
    #print 'M��ת��*M is : \n',np.dot(M.T,M)
    #print 'M*M��ת�� is ��\n',np.dot(M,M.T)
    print 'M*M��ת�� �����������Ϊ ��\n',np.linalg.eig(np.dot(M,M.T))
