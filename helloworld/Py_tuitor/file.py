'''
Created on Nov 20, 2014

@author: khiemtd
'''
name =raw_input('Nhap ten file')
f= open(name,'w')
f.write('dong so 1 \n')
#f.read()
f.close()

k=open(name)
print k.read()
k.close()