'''
Created on Dec 2, 2014

@author: khiemtd
'''
import os, glob
print os.getcwd()

#===============================================================================
# os.remove('newtemp')
# f=open('tempnha','w')
# f.write('adaada')
# f.close()
# os.rename('tempnha', 'newtemp')
# os.remove('newtemp')
#===============================================================================

#===============================================================================
#os.chdir('../')
print os.listdir('.')
# #print os.listdir('/home')
# print os.getcwd()
#===============================================================================

#===============================================================================
# # print file or directory
# for item in os.listdir('.'):
#     if os.path.isfile(item):
#         print 'item: %s is file'%item
#     elif os.path.isdir(item):
#         print 'item: %s is  directory'%item
#     else:
#         print 'unknown'
#===============================================================================

#===============================================================================
# a = os.path.join('*.py', '.') # find file name *.py
# for i in glob.glob(a):
#     print i
#===============================================================================

# print info file in directory
#===============================================================================
# i = -2;
# 
# path = raw_input('Enter path to traversal directory:')
# 
# for dirpath,dirnames , files in os.walk(path,topdown = True):
#     for name in files:
#         print "File %s, size %s, creation time %s, path: %s" \
#         % (name,\
#            os.stat(os.path.join(dirpath,name)).st_size,\
#            os.stat(os.path.join(dirpath,name)).st_ctime/3600,\
#            os.path.join(dirpath,name))
#===============================================================================
print os.stat(os.path.join('./','system.py')).st_ctime
    