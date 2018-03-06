'''license header
'''

import header
import body

f = open('mail.html','w')

headerMessage = header.header() 

#greetingsMessage = greetings.greetings()
body = body.body()
'''
<body><p>Hello World!</p></body>
</html>'''

message = headerMessage + body
f.write(message)
f.close()
