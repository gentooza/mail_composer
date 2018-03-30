'''license header
'''

import compose
import parameters
from mySmtp import mySmtp

f = open('mail.html','w')

'''compose mail'''
message = compose.composeMail()
'''send it?'''

f.write(message)
f.close()

mail = mySmtp()
if not mail.connect (parameters.smtpServer, parameters.smtpUser, parameters.smtpPassw):
    mail.setRecipients(parameters.recipients)
    mail.setSender(parameters.sender)
    mail.sendMail(message)
else:
    print("ERROR CONNECTIONG TO SERVER")

