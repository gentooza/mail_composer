# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:27:19 2017

@author: gentooza
"""
'''license header
'''

import parameters


def header():
    if(parameters.costumerLogo != ""):
        message = """<head><center><img src=\"""" + parameters.ourLogo + """\"alt=\"our logo here\" height=\"150\" width=\"200\"></center>
        <center><img src=\"""" + parameters.costumerLogo + """\"alt=\"your logo here\" height=\"150\" width=\"200\"></center></head>
        """
    else:
         message = """<head><center><img src=\"""" + parameters.ourLogo + """\"alt=\"our logo here\" height=\"150\" width=\"200\"></center>
        </head>"""
        
    return message
