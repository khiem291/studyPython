'''
Created on May 15, 2015

@author: KHIEM
'''
'E1'
#===============================================================================
# Q1:  Why change d2[‘y’] affects d[‘y’]?
# Because dictionary is a mutual type. Line: d2 = d and d2['y'] = 1 made d, d2 point to the same memory (no new memory allocated).
# Q2:  How to keep d[‘y’] as it was before?
# Purpose is allocate new memory for d2, use following code instead d=d2
# import copy
# d2 = copy.deepcopy(d)
#===============================================================================

#http://www.python-course.eu/deep_copy.php

'E2'
#===============================================================================
# Q1: Why change d2[‘y’][‘y1’] affects d[‘y’][‘y1’]?
# copy() created a new container populated with references to the contents of the original object. (shallow copy)
# copy() does not duplicate d, it reference d2 to d.
# 
# Q2: How to keep d[‘y’] as it was before?
# We can use deepcopy, this method completely duplicate d 
#===============================================================================

'E3'
#===============================================================================
# Indentify issues and refactor the function above
# -if, if ... do not include all cases (missing)
# -it does not good view 
# -it's hard to indentify invalid (default) value 
# 
# So, if elif else is better
#===============================================================================

'E4'
def getTargetStation(dd, gg):
    print 'get'
sta_ips =0
count = 0
while True:
    sta_11g = getTargetStation(sta_ips,"Pick an 11g wireless station: ")
    sta_11n = getTargetStation(sta_ips, "Pick an 11n 2.4G wireless station: ")
    sta_11n50 = getTargetStation(sta_ips, "Pick an 11n 5.0G wireless station: ")
    sta_11a = getTargetStation(sta_ips, "Pick an 11a wireless station: ")

    if (sta_11g or sta_11n or sta_11n50 or sta_11a): break
    else:
        count +=1
        if count == 10:
            print "Pick at least one station as your target"
            break

# Identify issues and refactor the code block above
# I think it can be loop in some cases if method  getTargetStation FAIL
# We should add retry 10 times in oder to avoid looping