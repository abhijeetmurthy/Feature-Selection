
from fileinput import filename
import numpy as np
from numpy import genfromtxt as readtxt
import time
import warnings
warnings.filterwarnings("ignore")
from helper import *
from forward_selection import forward_selection
from backward_elimination import backward_elimination


def main():
    filename="large.txt"
    data = readtxt(filename)
    # algo = int(input())
    # algo=1
    strstr = 'This dataset has {} features, with {} instances\n'.format(data.shape[1]-1, data.shape[0])
    strstr += 'Running nearest neighbor with all {} features, accuracy of {}%\n'.format(data.shape[1]-1, evaluation(data))
    print(strstr)

    # start = time.time()
    # if(algo == 1):
    forward_selection(data, filename.split(".")[0])
    # elif(algo == 2):
    backward_elimination(data, filename.split(".")[0])
    # else: 
    #     return


    # end = time.time()
    # print("Time to finish: {}".format(end-start))


if __name__ == "__main__":

    main()
    