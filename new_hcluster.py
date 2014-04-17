# -*- coding: cp936 -*-
'''
改进的层次聚类算法
@author slhuang
2014-3-17
++++++++++++++++++++++
1、将每个对象归为一类, 共得到N类, 每类仅包含一个对象. 类与类之间的距离就是它们所包含的对象之间的距离.
2、找到最接近的两个类并合并成一类, 于是总的类数少了一个.
3、采用最短距离方法，重新计算新的类与所有旧类之间的距离.
4、重复第2步和第3步, 直到最后合并成一个类为止(此类包含了N个对象).
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
    clusters = [ [i+1] for i in range(len(matrix)) ] #初始化，分成N类
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
                    
        c1,c2 = flag #解包c1 = i , c2 = j
     #  print flag
        clusters[c1]= clusters[c1] + clusters[c2]
        del clusters[c2]
    #    print clusters
        
        #data[c1]=[getmin(data[c1][i],data[c2][i]) for i in range(data_len)] #形成新的类中心，最短距离
        data[c1]=[(data[c1][i]+data[c2][i])/2 for i in range(data_len)] #形成新的类中心，中心
        
        del data[c2]  #删除一行
        for item in data:
            del item[c2]     #删除一列   

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
