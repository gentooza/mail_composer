'''license header
'''

import header
import body
import end

def composeMail():
    message = '''
    <!DOCTYPE html>
    <html>
    <link href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i" rel="stylesheet">
    '''
    message = header.header() + body.body() + end.end()
    return message