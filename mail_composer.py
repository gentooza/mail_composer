logo = "custom.bmp"

f = open('mail.html','w')

header = """<html>
"""
logo = """<head><center><img src=\"""" + logo + """\"alt=\"company logo\" height=\"150\" width=\"200\"></center></head>"""


body = """
<body><p>Hello World!</p></body>
</html>"""

message = logo+body
f.write(message)
f.close()