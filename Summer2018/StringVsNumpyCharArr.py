from array import array
import numpy as np
import sys, timeit

def String():
    out_str = ''
    idx=0
    for num in range(loop_count):
        out_str += 'num'
        idx+=len('num')
    return out_str

def ListChar():
    str_list = []
    idx=0
    for num in range(loop_count):
        str_list.append('num')
        idx+=len('num')
    out_str = ''.join(str_list)
    return out_str

def ListCompListChar():
    idx=0
    for num in range(loop_count):
        idx+=len('num')
    out_str = ''.join(['num' for num in range(loop_count)])
    return out_str

def ListCompString():
    idx=0
    for num in range(loop_count):
        idx+=len('num')
    out_str = ''.join('num' for num in range(loop_count))
    return out_str

char_arr = np.empty(shape=(1024*1024), dtype='|S1')
def NumpyCharArr1():
    idx=0
    for num in range(loop_count):
        char_arr[idx:idx+len('num')] = [x for x in 'num']
        idx+=len('num')
    return char_arr[0:idx-len('num')].tostring().decode('utf-8')

def NumpyCharArr():
    char_arr1 = np.empty(shape=(1024*1024), dtype='|S1')
    idx=0
    for num in range(loop_count):
        char_arr1[idx:idx+len('num')] = 'num'
        idx+=len('num')
    return char_arr1[0:idx-len('num')].tostring().decode('utf-8')

def NumpyArry():
    out_str = np.chararray(shape=(1024*1024))
    idx=0
    for num in range(loop_count):
        char_arr[idx:idx+len('num')] = [x for x in 'num']
        idx+=len('num')
    return out_str.tostring()

loop_count = 80000
print (sys.version)
#
print ('String=', timeit.timeit(String, number=100))
print ('ListChar=', timeit.timeit(ListChar, number=100))
print ('ListCompListChar=', timeit.timeit(ListCompListChar, number=100))
print ('ListCompString=', timeit.timeit(ListCompString, number=100))
print ('NumpyCharArr=', timeit.timeit(NumpyCharArr, number=100))
print ('NumpyCharArr1=', timeit.timeit(NumpyCharArr1, number=100))
print ('NumpyArry=', timeit.timeit(NumpyArry, number=100))
