# -*- coding: cp936 -*-
''' 
寻找频繁项集  A-priori 算法
@author slhuang
2014-4-12
'''

import copy
import gc  #内存释放
import time


def get_basket_item(basketnum): #获得事务项，一般是从数据库或文件中读取
    basket_item=[[] for i in range(basketnum)]
    for basket_num in range(1,basketnum+1):
        for item_num in range(1,basket_num+1):
            model=basket_num%item_num
            if(model==0):
                basket_item[basket_num-1].append(item_num)
    return basket_item



def get_items(basket_item):  #获得所有item  #这个函数在本A-Priori算法中用到，实际应用当中，应该使用下面的get_freq_item()函数
    items=[]
    for itemset in basket_item:
        for item in itemset:
            if [item] not in items:
                items.append([item])            
    return items



def get_freq_item(basket_item,freq): #通常情况下，往往不知道购物篮里一共有多少item，所以第一遍扫描的时候，有必要先统计出所有的item，最好能够计数
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

def get_item_freqNum(basket_item,item):   #计算item出现的次数，然后与最小支持度进行比较
    cnt_item=0
    for basket_num in range(1,len(basket_item)+1):
        num=len(item)
        for i in range(len(item)):
            if item[i] in basket_item[basket_num-1]:
                num-=1
        if num == 0:
            cnt_item+=1
    return float(cnt_item)


def get_confidence(basket_item,itemA,itemB): #求置信度
    itemAB=itemA+itemB
    return float(get_item_freqNum(basket_item,itemAB)/get_item_freqNum(basket_item,itemA))


def get_pair_matrix(freq_item): #合并频繁项集，产生高层的频繁候选集
    if len(freq_item)==1 :
        freq_pair=freq_item
    else:
        freq_pair=[]
    for i in range(len(freq_item)):
        for j in range(i+1,len(freq_item)):
            pair=list( set.union( set(freq_item[i]),set(freq_item[j]) ) ) #求两个list的去重后的并集
            if len(pair)==len(freq_item[i])+1 : #依次获得2,3,4,5...项集
                pair.sort()
                if pair not in freq_pair:
                    freq_pair.append(pair)             
    return freq_pair
            
def a_priori_freq_items(basket_item,support,output_file_name):   #A-Priopi算法核心
    freq_item_before=get_items(basket_item)
    freq_item_after=[]
    freq_item_num=0
    outputfile=open(output_file_name,'w')
    while(freq_item_after!=freq_item_before):   #结束条件，已经找不到合并的频繁项集了
        freq_item_after=copy.copy(freq_item_before) #浅拷贝
        for item in freq_item_before :
            if get_item_freqNum(basket_item,item)<support :  #支持度阀值
                freq_item_after.remove(item)  #获得的频繁项集
        if freq_item_after==[]:
            break
        else:
            freq_item_num+=1
            print 'Support=%d. freq %d itemset:\n'%(support,freq_item_num),freq_item_after  
            outputfile.write('Support=%d. freq %d itemset:\n'%(support,freq_item_num)+str(freq_item_after)+'\n')            
            if(freq_item_after!=freq_item_before):
                del freq_item_before
                gc.collect()
                freq_item_before=get_pair_matrix(freq_item_after) #获得高层候选项集
    outputfile.close()
    return freq_item_before
                        
            
if __name__=='__main__' :
    
    all_items=[[i] for i in range(1,7)]
    pair_items=get_pair_matrix(all_items)
    
    basket_item=[[1,2,3],[2,3,4],[3,4,5],[4,5,6],
                 [1,3,5],[2,4,6],[1,3,4],[2,4,5],
                 [3,5,6],[1,2,4],[2,3,5],[3,4,6]]

   # for item in all_items:
   #     print 'item %s support is:' %item,get_item_freqNum(basket_item,item)

    for pair_item in pair_items:
        #print 'item %s support is:' %pair_item,get_item_freqNum(basket_item,pair_item)
        if (get_item_freqNum(basket_item,pair_item)>=4) :
            print 'freq itemset %s will hash to %d bucket' %(pair_item,(pair_item[0]*pair_item[1])%11)

    '''
    items=[[i] for i in range(1,21)]
    a=get_pair_matrix(items)
    print 'items number is 20, the pair of a[100] is:',a[100]
    '''
    '''
    N=100
    support=5    
    basket_item=get_basket_item(N)
    output_file_name='freq_itemset.txt'
    a_priori_freq_items(basket_item,support,output_file_name)
    '''
    
    '''    
    itemA=[5,7]
    itemB=[2]
    print '{5,7}->2 Confidence: %f' %get_confidence(basket_item,itemA,itemB)
    itemC=[2,3,4]
    itemD=[5]
    print '{2,3,4}->5 Confidence: %f' %get_confidence(basket_item,itemC,itemD)
    
    print 'freq item is :'
    print get_freq_item(basket_item,5)
    '''

            
