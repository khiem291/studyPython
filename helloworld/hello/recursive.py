'''
Created on Feb 21, 2014

@author: khiemtd
'''
'''
def tinnh(L):
    if not L:
        return 0
    else:
        return L[0]+ tinnh(L[1:])
L=([1,2,3,4,5])
print tinnh(L)
'''
from StcPython import StcPython
stc = StcPython()
#print stc.get('system1', 'version')

chassisAddress = '172.33.42.4'
slot = 4
port = 3
print "using //%s/%s/%s" % (chassisAddress, slot,  port)

#stc.connect('172.33.42.4')
#stc.reserve('//172.33.42.4/4/3')

print 'Create a Project  - root'

project = stc.create('project')

print 'Get Project attributes'

projectAtt = stc.get(project, 'name')

print projectAtt
print 'Create Ports under',  project

port1 = stc.create('port', under=project)
print 'Configure Port locations'
stc.config(port1, location="//%s/%s/%s" % (chassisAddress, slot,  port))

print 'Creating StreamBlock on Port  1'
streamBlock = stc.create('streamBlock', under=port1  )
generator = stc.get(port1, 'children-generator')

print 'Attaching Ports...'

stc.perform('AttachPorts', portList=[port1], autoConnect='TRUE')
stc.apply()

print 'Call Subscribe...'

port1GeneratorResult  = stc.subscribe(Parent=project,
                                      ResultParent=port1,
                                      ConfigType='Generator',
                                      resulttype='GeneratorPortResults',
                                      filenameprefix="Generator_port1_counter_%s" % port1,
                                      Interval=2)

print 'Starting Traffic...'
# wait for analyzer to start 
stc.sleep(10)
stc.perform('GeneratorStart', generatorList=generator)
print "start", generator 
# generate traffic for  5 seconds 
print 'Sleep 5 seconds...'
stc.sleep(5)
print 'Stopping Traffic...'

stc.perform('GeneratorStop', generatorList=generator)

print 'stop', generator

print 'Call Unsubscribe...'

stc.unsubscribe(port1GeneratorResult)

stc.sleep(10)