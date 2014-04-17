# -*- coding: cp936 -*-
''' 
Ѱ��Ƶ���  A-priori �㷨
@author slhuang
2014-4-12
'''

import copy
import gc  #�ڴ��ͷ�
import time


def get_basket_item(basketnum): #��������һ���Ǵ����ݿ���ļ��ж�ȡ
    basket_item=[[] for i in range(basketnum)]
    for basket_num in range(1,basketnum+1):
        for item_num in range(1,basket_num+1):
            model=basket_num%item_num
            if(model==0):
                basket_item[basket_num-1].append(item_num)
    return basket_item



def get_items(basket_item):  #�������item  #��������ڱ�A-Priori�㷨���õ���ʵ��Ӧ�õ��У�Ӧ��ʹ�������get_freq_item()����
    items=[]
    for itemset in basket_item:
        for item in itemset:
            if [item] not in items:
                items.append([item])            
    return items



def get_freq_item(basket_item,freq): #ͨ������£�������֪����������һ���ж���item�����Ե�һ��ɨ���ʱ���б�Ҫ��ͳ�Ƴ����е�item������ܹ�����
    items=[]
    count=[]
    freq_item=[]
    for itemset in basket_item:
        for item in itemset:
            if item not in items:
                items.append(item)
                count.append(1)
            else:
                count[items.index(item)]+=1
    for index in range(len(count)):
        if count[index]>=freq :
            freq_item.append([items[index]])
            
    return freq_item

def get_item_freqNum(basket_item,item):   #����item���ֵĴ�����Ȼ������С֧�ֶȽ��бȽ�
    cnt_item=0
    for basket_num in range(1,len(basket_item)+1):
        num=len(item)
        for i in range(len(item)):
            if item[i] in basket_item[basket_num-1]:
                num-=1
        if num == 0:
            cnt_item+=1
    return float(cnt_item)


def get_confidence(basket_item,itemA,itemB): #�����Ŷ�
    itemAB=itemA+itemB
    return float(get_item_freqNum(basket_item,itemAB)/get_item_freqNum(basket_item,itemA))


def get_pair_matrix(freq_item): #�ϲ�Ƶ����������߲��Ƶ����ѡ��
    if len(freq_item)==1 :
        freq_pair=freq_item
    else:
        freq_pair=[]
    for i in range(len(freq_item)):
        for j in range(i+1,len(freq_item)):
            pair=list( set.union( set(freq_item[i]),set(freq_item[j]) ) ) #������list��ȥ�غ�Ĳ���
            if len(pair)==len(freq_item[i])+1 : #���λ��2,3,4,5...�
                pair.sort()
                if pair not in freq_pair:
                    freq_pair.append(pair)             
    return freq_pair
            
def a_priori_freq_items(basket_item,support,output_file_name):   #A-Priopi�㷨����
    freq_item_before=get_items(basket_item)
    freq_item_after=[]
    freq_item_num=0
    outputfile=open(output_file_name,'w')
    while(freq_item_after!=freq_item_before):   #�����������Ѿ��Ҳ����ϲ���Ƶ�����
        freq_item_after=copy.copy(freq_item_before) #ǳ����
        for item in freq_item_before :
            if get_item_freqNum(basket_item,item)<support :  #֧�ֶȷ�ֵ
                freq_item_after.remove(item)  #��õ�Ƶ���
        if freq_item_after==[]:
            break
        else:
            freq_item_num+=1
            print 'Support=%d. freq %d itemset:\n'%(support,freq_item_num),freq_item_after  
            outputfile.write('Support=%d. freq %d itemset:\n'%(support,freq_item_num)+str(freq_item_after)+'\n')            
            if(freq_item_after!=freq_item_before):
                del freq_item_before
                gc.collect()
                freq_item_before=get_pair_matrix(freq_item_after) #��ø߲��ѡ�
    outputfile.close()
    return freq_item_before
                        
            
if __name__=='__main__' :
    N=100
    support=5    
    basket_item=get_basket_item(N)
    output_file_name='freq_itemset.txt'
    a_priori_freq_items(basket_item,support,output_file_name)
    
    

            
