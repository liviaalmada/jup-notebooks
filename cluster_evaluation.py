import pandas as pd
from scipy import stats as st

def compactness(cluster):
    n = 1
    x = 0
    print(len(cluster))
    for i in range(0,len(cluster)):
        for j in range(0,len(cluster)):
            if(i!=j):       
                stat = st.kstest(st.norm.rvs(size=100, loc=cluster[i,4], scale=cluster[i,5]),"norm", args=(cluster[j,4],cluster[j,5]))
                x = x + stat.statistic 
                
    return x/(len(cluster)*(len(cluster)-1)*2)


def separation(cluster1, cluster2):
    n = 0
    x = 0
    for i in range(0,len(cluster1)):
        for j in range(0,len(cluster2)):
            stat = st.kstest(st.norm.rvs(size=100, loc=cluster1[i,4], scale=cluster1[i,5]),"norm", args=(cluster2[j,4],cluster2[j,5]))
            x = x + stat.statistic 
            n=n+1
    return x/n    

def compactness_mean(clusters):
    sum_comp = 0
    for c in clusters:
        sum_comp = sum_comp + compactness(c)
      
    return sum_comp / len(clusters)

def separation_mean(clusters):
    sum_comp = 0
    for c1 in range(0,len(clusters)):
        for c2 in range(0,len(clusters)):
            if(c1!=c2):
                sum_comp = sum_comp + separation(clusters[c1],clusters[c2])
    return sum_comp / (len(clusters)*(len(clusters)-1))