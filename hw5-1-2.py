
import pandas as pd
import numpy as np
path='F:\Data\data1.csv'
df=pd.read_csv(path)

import matplotlib.pyplot as plt
plt.plot(df.x,df.y,'bo')
plt.show()

def print_cluster(c1p,c2p,c3p,cs):

    z=np.array(cs)
    
    try:
        plt.plot(c1p[:,0],c1p[:,1],'ro')
        plt.plot(c2p[:,0],c2p[:,1],'go')
        plt.plot(c3p[:,0],c3p[:,1],'yo')
        plt.plot(z[:,0,0],z[:,0,1],'bx')
    except:
        print('I\'v choose 2 same node, and it appier in two cluster ')


from math import sqrt

def distant(nod1,nod2):
    return sqrt(((float(nod1.x)-nod2[0])**2)+((float(nod1.y)-nod2[1])**2 ))

def distant_nod_from_line(nod1,nod2,nod3):
    return ( abs( (float(nod1.y)-nod2[1])*nod3.x + (nod2[0]-float(nod1.x))*nod3.x ) )

d = lambda s: distant_nod_from_line(cs1,cs[0][0],s)
    
d1 = lambda s: distant(s,cs[0][0])
d2 = lambda s: distant(s,cs[1][0])
d3 = lambda s: distant(s,cs[2][0])


cs=[np.array(df.sample())]
cs1_index=df.agg(d1,axis=1).idxmax()
cs1=df[cs1_index:cs1_index+1]
dfe=df.drop(cs1_index)
cs2_index=dfe.agg(d,axis=1).idxmax()
cs2=df[int(cs2_index):int(cs2_index)+1]

#append centroid
cs.append(np.array(cs1))
cs.append(np.array(cs2))
##___________________________________moshabeh ghabl

#start algoritm
csn= [np.array([0,0]) for x in range(3)]
stop=0
n=0
itt=10
while(stop==0):
    #stoping algoritm
    if((np.array_equal(cs[0],csn[0]))&(np.array_equal(cs[1],csn[1]))
        &(np.array_equal(cs[2],csn[2]))): #has converged 
        stop=1
        print('algoritm has stoped in ',n,' step')
        break
    elif n==itt: #achive to ittation stop cercumstances
        stop=1
        break
    elif n>0 : #set the new centroid
        cs[0]=csn[0]
        cs[1]=csn[1]
        cs[2]=csn[2]
    else:       #n=0 the algorytm has start
        print('algoritm has started')
    
    #calculate distant ,distant of each data ,from him centroid
    l1=df.agg(d1,axis=1)
    l2=df.agg(d2,axis=1)
    l3=df.agg(d3,axis=1)

    #blanking clusters list
    c1=list()
    c2=list()
    c3=list()

    #clustering data 
    for i in range(len(df)):
        a=[l1[i],l2[i],l3[i]]
        cat=a.index(min(a))
        if cat==0:
            c1.append(df.values[i])
        elif cat==1:
            c2.append(df.values[i])
        else:#cat=3
            c3.append(df.values[i])
    #update centroid
    c1p=np.array(c1)
    c2p=np.array(c2)
    c3p=np.array(c3)
     
    csn[0]=np.array([[np.mean(c1p[:,0]),np.mean(c1p[:,1])]])
    csn[1]=np.array([[np.mean(c2p[:,0]),np.mean(c2p[:,1])]])
    csn[2]=np.array([[np.mean(c3p[:,0]),np.mean(c3p[:,1])]])
    
    n=n+1
    print_cluster(c1p,c2p,c3p,cs)
    plt.show()  




