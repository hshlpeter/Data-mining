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
    #print clusters
    while(len(data)>k):
        min_val=data[0][1]
        flag=(0,1)
     #   print data
        data_len=len(data)
        #print data_len
        for i in range(data_len-1):
            for j in range(i+1,data_len):
                if(data[i][j]<min_val):
                    min_val=data[i][j]
                    flag=(i,j)
                    
        c1,c2 = flag #���c1 = i , c2 = j
     #  print flag
        clusters[c1]= clusters[c1] + clusters[c2]
        del clusters[c2]
    #    print clusters
        
        #data[c1]=[getmin(data[c1][i],data[c2][i]) for i in range(data_len)] #�γ��µ������ģ���̾���
        data[c1]=[(data[c1][i]+data[c2][i])/2 for i in range(data_len)] #�γ��µ������ģ�����
        
        del data[c2]  #ɾ��һ��
        for item in data:
            del item[c2]     #ɾ��һ��   

    return clusters


def readFile(fileName,row_num,col_num):
    matrix = [[0 for col in range(col_num)] for row in range(row_num)]
    f = file(fileName,'r')
    cnt = 0
    for line in f.readlines():
        line_sp = line.rstrip().split(',')
        #line_sp = line.rstrip().split(' ')
        for i in range(len(line_sp)):
            if(line_sp[i].find('E')>0):
                data=line_sp[i].rstrip().split('E-')
                vaule1=float(data[0])/(10^int(data[1]))
                if(vaule1 < 0.0 ):
                    vaule1 = 0.0
                if(vaule1 > 1.0 ):
                    vaule1 = 0.9999
                matrix[cnt][i]= math.degrees(math.acos(vaule1))
            else:
                if(line_sp[i] == 'NaN'):
                    line_sp[i]=0.0
                if(line_sp[i]!=''):
                    vaule2=float(line_sp[i])
                    if(vaule2 > 1.0):
                        vaule2 = 0.9999
                    if(vaule2 < 0.0):
                        vaule2 = 0.0
                    matrix[cnt][i] = math.degrees(math.acos(vaule2))
                    #print matrix[cnt][i]
        cnt += 1
        
    f.close()
    return matrix

matData = readFile('3_cos_sim.txt',884,884)

#matData=[[0,622,877,255,412,996],[662,0,295,468,268,400],[877,295,0,754,564,138],[255,468,754,0,219,869],[412,268,564,219,0,669],[996,400,138,869,669,0]]

l=cluster(matData,50)

print l

#print len(matData)

#del matData[0]
#for item in matData:
#    del item[0]

#print matData
