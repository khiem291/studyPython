'''
Created on Apr 16, 2015

@author: khiemtd
'''
import sqlite3, types

class DefectModel(object):
    
    def getDefectList(self, component):
    
        query = 'select ID from defect where component = "%s"'%component
        defectList = self._dbselect(query)
        #print defectList
        lst = []
        for row in defectList:
            #print row
            lst.append(row[0])
        #print 'getDefectList',lst
        return lst
    
    def getSummary(self, fid): 
        
        query = "select summary from defect where ID = '%d' " % fid 
        summary = self._dbselect(query) 
        #print summary
        for row in summary: 
            #print 'getSummary',row[0] 
            return row[0] 
    
    def _dbselect(self, query):
        connection = sqlite3.connect('TMS') 
        #cursorObj = connection.cursor() 
        #results = cursorObj.execute(query) 
        results = connection.execute(query)
        connection.commit() 
        #cursorObj.close()
        #connection.close() 
        return results 
    
class DefectView():
    
    def sumary(self, sumary, defectid):
        print '### Defect Summary for defect #%d ###\n%s'% (defectid, sumary)
    
    def defectList(self, list, category): 
        print "#### Defect List for %s ####\n" % category 
        for defect in list: 
            print defect 

class Controler:
    
    def getDefectsumary(self, defectid):
        model = DefectModel()
        view = DefectView()
        sum_data = model.getSummary(defectid)
        return view.sumary(sum_data, defectid)
    
    def getDefectList(self, component):
        model = DefectModel()
        view = DefectView()
        def_data = model.getDefectList(component)
        return view.defectList(def_data, component)
    
#a= DefectModel()
#a.getDefectList('XYZ')
#a.getSummary(2)
#Using
#import mvc
b =  Controler()
b.getDefectList('XYZ')
b.getDefectsumary(3)

