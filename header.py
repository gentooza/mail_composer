# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:27:19 2017

@author: gentooza
"""
'''license header
'''

import parameters


def header():
    message = '''<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <style>
    body  
    {
        font-family: 'Roboto';    
    }
    </style>'''
    if(parameters.costumerLogo != ""):
        message += '''<center><img src=\"''' + parameters.ourLogo + '''\"alt=\"our logo here\" height=\"150\" width=\"200\"></center>
        <center><img src=\"''' + parameters.costumerLogo + '''\"alt=\"your logo here\" height=\"150\" width=\"200\"></center></head>
        '''
    else:
         message += '''<center><img src=\"''' + parameters.ourLogo + '''\"alt=\"our logo here\" height=\"150\" width=\"200\"></center>'''
    message += '''</head>'''
        
    return message
