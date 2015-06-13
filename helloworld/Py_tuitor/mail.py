'''
Created on Oct 15, 2014

@author: khiemtd
'''
#!/usr/bin/python 
 
import smtplib 


sender = 'anpd@atvn.com.vn' 
receivers = ['trientl@atvn.com.vn',] 
 
message = """From: <anpd@yahoo.com.vn> 
To: <trientl@atvn.com.vn>
Subject: Love
 
nothing
 
""" 
 
try: 
    smtpObj = smtplib.SMTP('hcmcexch2.atvn.com.vn') 
    for i in range(1):
        smtpObj.sendmail(sender, receivers, message)          
    print "Successfully sent email by Python"
    
except Exception,e:#SMTPException: 
    print "Error: unable to send email \n", e 