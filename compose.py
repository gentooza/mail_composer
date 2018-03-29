'''license header
'''

import header
import body
import end

def composeMail():
    message = header.header() + body.body() + end.end()
    return message