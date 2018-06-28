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

def NumpyCharArr():
    char_arr = np.empty(shape=(1024*1024), dtype='|S1')
    idx=0
    for num in range(loop_count):
        char_arr[idx:idx+len('num')] = 'num'
        idx+=len('num')
    return char_arr[0:idx-len('num')].tostring().decode('utf-8')

loop_count = 8000
print (sys.version)
#
print ('String=', timeit.timeit(String, number=10))
print ('ListChar=', timeit.timeit(ListChar, number=10))
print ('ListCompListChar=', timeit.timeit(ListCompListChar, number=10))
print ('ListCompString=', timeit.timeit(ListCompString, number=10))
print ('NumpyCharArr=', timeit.timeit(NumpyCharArr, number=10))