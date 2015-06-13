'''
Created on Oct 7, 2014

@author: khiemtd
'''
print 'Prime: ',
for i in range(1, 100):
    if i in [1, 2]:
        print i,
    else:
        for b in range(2, i):
            if i % b == 0:
                # print i,
                break
        else:        
            print i,

