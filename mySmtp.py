#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:40:32 2018

@author: gentooza
"""

'''license header
'''

import smtplib
from email.mime.text import MIMEText


class mySmtp:
    def __init__(self, host, user, passw):
        self.recipients = []
        self.sender = ""
        
    def connect(self, host, user, passw):
         try:
             self.smtpConn = smtplib.SMTP(host)
             self.smtpConn.login(user,passw)
             return 0
         except:
             return -1      
        
    def pushRecipient(self,recipient):
        self.recipients.append(recipient) 
        
    def setRecipients(self,recipients):
        self.recipients = recipients
        
    def setSender(self,sender):
        self.sender = sender
        
    def sendMail(self,message):
        mail = MIMEText(message,'html')
        mail['Subject'] = "mail prueba"
        mail['From'] = self.sender    
        mail['To'] = ", ".join(self.recipients)
        self.smtpConn.sendmail(self.sender,self.recipients,mail.as_string())
      
        