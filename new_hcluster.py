# -*- coding: cp936 -*-
'''
�Ľ��Ĳ�ξ����㷨
@author slhuang
2014-3-17
++++++++++++++++++++++
1����ÿ�������Ϊһ��, ���õ�N��, ÿ�������һ������. ������֮��ľ�����������������Ķ���֮��ľ���.
2���ҵ���ӽ��������ಢ�ϲ���һ��, �����ܵ���������һ��.
3��������̾��뷽�������¼����µ��������о���֮��ľ���.
4���ظ���2���͵�3��, ֱ�����ϲ���һ����Ϊֹ(���������N������).
++++++++++++++++++++++
'''
#encoding:utf-8
import math

def getmin(dis1,dis2):
    if dis1<dis2:
        return dis1
    else:
        return dis2


def cluster(matrix,k):
    data=matrix
    clusters = [ [i+1] for i in range(len(matrix)) ] #��ʼ�����ֳ�N��
    while(len(data)>k):
        min_val=data[0][1]
        flag=(0,1)
        data_len=len(data)
        #print data_len
        for i in range(data_len-1):
            for j in range(i+1,data_len):
                if(data[i][j]<min_val):
                    min_val=data[i][j]
                    flag=(i,j)
                    
        c1,c2 = flag #���c1 = i , c2 = j

        clusters[c1]= clusters[c1] + clusters[c2]
        del clusters[c2]
        
        #data[c1]=[getmin(data[c1][i],data[c2][i]) for i in range(data_len)] #�γ��µ������ģ���̾���
        data[c1]=[(data[c1][i]+data[c2][i])/2 for i in range(data_len)] #�γ��µ������ģ�����
        
        del data[c2]  #ɾ��һ��
        for item in data:
            del item[c2]     #ɾ��һ��
            
    return clusters


if __name__='__main__':
    matData=[[0,622,877,255,412,996],[662,0,295,468,268,400],[877,295,0,754,564,138],[255,468,754,0,219,869],[412,268,564,219,0,669],[996,400,138,869,669,0]]
    print cluster(matData,2)


