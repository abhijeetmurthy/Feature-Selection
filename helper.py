import numpy as np
from operator import itemgetter
from collections import Counter

def evaluation(data):
    predicted_values = []
    data_classes = [entry[0] for entry in data]

    for index in range(len(data)):
        x = data[index]
        x = x[1:]
        X = []
        if index == 0:
            X = data[1:]
        elif index == (len(data)-1):
            X = data[:index]
        else:
            X = np.concatenate((data[:index],data[index+1:]), axis=0)
        Y = [i[0] for i in X]
        X = np.delete(X, 0, axis=1)
        predicted = model(x, X, Y, 2)
        predicted_values.append(predicted)
    
    accuracy = get_accuracy(predicted_values, data_classes)
    return accuracy
    

def metric(x,y,p):
    d = 0
    for i,j in zip(x,y):
        temp = (abs(i-j)**p)
        d += temp
    return (d**(1/p))

def model(x, X, Y, p):
    y = []
    k = 1
    allDistances = []
    trainCnt = 0
    for dataEntry in X:
        newDistance = metric(dataEntry, x, p)
        allDistances.append((newDistance, Y[trainCnt]))
        trainCnt += 1
    allDistances = sorted(allDistances, key=itemgetter(0))
    neighbors = [val[1] for val in allDistances[:k]]
    countClass = list(Counter(neighbors).keys())
    y.append(countClass[0])
    return y


def get_accuracy(y, class_data):
    sameCount = 0
    for i,j in zip(y, class_data):
        if i == j:
            sameCount += 1
    accuracy = (sameCount/len(class_data)) * 100
    return accuracy
