# -*- coding:utf-8 -*-
'''
print api example: print('output is: ' + str(output))
'''
import numpy
import scipy.stats as sta
import matplotlib.plot_api as plt


# from print_api import print

def first_year():
    X = sta.norm(loc=950,
                 scale=20)  # generate random data in normal distribution whose expectation is 950 and standard deviation is 20
    wbread = []
    for i in range(365):
        x = X.rvs(size=100)
        wbread.append(x[0])  # get the random data for one day

    # log(numpy.mean(wbread))#print mean value
    # log(sta.skew(wbread))#print skew value
    print(numpy.mean(wbread))  # print mean value
    print(sta.skew(wbread))  # print skew value
    plt.hist(wbread, color='grey')
    plt.savefig('first_year.png')


def second_year():
    X = sta.norm(loc=950,
                 scale=20)  # generate random data in normal distribution whose expectation is 950 and standard deviation is 20
    wbread = []
    for i in range(365):
        x = X.rvs(size=100)
        wbread.append(max(x))  # get the random data for one day

    # log(numpy.mean(wbread))#print mean value
    # log(sta.skew(wbread))#print skew value
    print(numpy.mean(wbread))  # print mean value
    print(sta.skew(wbread))  # print skew value
    plt.hist(wbread, color='grey')
    plt.savefig('second_year.png')


# the code should not be changed
if __name__ == '__main__':
    first_year()
    second_year()
