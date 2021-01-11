import pandas as pd
import numpy as np

import math
import matplotlib.pyplot as plt
import random
 
    
def getEuclidean(point1, point2):
    dimension = len(point1)
    dist = 0.0
    for i in range(dimension):
        dist += (point1[i] - point2[i]) ** 2
    return math.sqrt(dist)
    
def k_means(dataset, k, iteration):

    #初始化簇心向量
    index = random.sample(list(range(len(dataset))), k)
    vectors = []
    for i in index:
        vectors.append(dataset[i])
    #初始化标签
    labels = []
    for i in range(len(dataset)):
        labels.append(-1)
    #根据迭代次数重复k-means聚类过程
    while(iteration > 0):
        #初始化簇
        C = []
        C1 = []
        for i in range(k):
            C.append([])
            C1.append([])
        leng = [0 for i in range(len(dataset))]    
        for labelIndex, item in enumerate(dataset):
            classIndex = -1
            minDist = 1e6
            for i, point in enumerate(vectors):
                dist = getEuclidean(item, point)
                if(dist < minDist):
                    classIndex = i
                    minDist = dist
                    leng[labelIndex] = getEuclidean(item, vectors[abs(1-i)])
            C[classIndex].append(item)
            C1[classIndex].append(labelIndex)
            labels[labelIndex] = classIndex
            

        while abs(len(C[0])- len(C[1]))>0.4*(len(C[0])+len(C[1])):
            if len(C[0])< len(C[1]):
                re1,re2 = 0,1
            else:
                re1,re2 = 1,0
            lis1 = [leng[s] for s in C1[re2]]
            index1 = C1[re2][lis1.index(min(lis1))]
            C[re1].append(dataset[index1])
            C[re2].remove(dataset[index1])
            C1[re1].append(index1)
            C1[re2].remove(index1)
            labels[index1] = re1
        for i, cluster in enumerate(C):
            clusterHeart = []
            dimension = len(dataset[0])
            for j in range(dimension):
                clusterHeart.append(0)
            for item in cluster:
                for j, coordinate in enumerate(item):
                    clusterHeart[j] += coordinate / len(cluster)
            vectors[i] = clusterHeart
        iteration -= 1
    return C, labels