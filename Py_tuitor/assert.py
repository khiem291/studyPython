'''
Created on Oct 9, 2014

@author: khiemtd
'''

def KelvinToFahrenheit(Temperature): 
   assert (Temperature >= 0),"Colder than absolute zero!" 
   return ((Temperature-273)*1.8)+32 
 
#print KelvinToFahrenheit(273) 
#print int(KelvinToFahrenheit(505.78)) 
#print KelvinToFahrenheit(-5) 

def Error(bien):
    try:
        if bien >0:
            raise TypeError('I hate you')
    except Exception,e:
        print e
Error(4)   
    