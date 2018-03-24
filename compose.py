'''license header
'''

import header
import body

def composeMail():
    message = header.header() + body.body()
    return message