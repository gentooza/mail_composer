'''license header
'''

import compose

f = open('mail.html','w')

'''compose mail'''
message = compose.composeMail()
'''send it?'''

f.write(message)
f.close()
