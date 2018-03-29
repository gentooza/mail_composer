#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''license header
'''
import parameters

def end():
    message = '''</p>
    <p> Para cualquier incidencia no duden en contactarnos a ''' + parameters.ourContact + '''</p>
    <p>Hata pronto!</p>
    </p>'''
    try:
        ourSignature = open(parameters.ourSignature,'r')
        message += '''</body> </html>''' + ourSignature.read()       
    except:
        message += '''<p> Un cariñoso abrazo de ''' + parameters.ourName  + '''</p></body> </html>'''
    
    return message
