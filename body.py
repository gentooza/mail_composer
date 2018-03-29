#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''license header
'''
import parameters

def body():
    message = '''<body><p>Hola '''
    if not parameters.costumerContact:
        message += parameters.costumerName
    else:
        message += parameters.costumercontact
    message += '''!</p>
    <p>Lo primero, Daros la bienvenida y las gracias por decidir trabajar con ''' + parameters.ourName + '''</p>
    <p>Hemos trabajado duro durante estos años para poder traer a los colectivos sociales y empresas de economía social, la solución al alojamiento web más profesional y coherente posible</p>
    '''
    message +='''</p>
    <p>Os escribimos este correo para explicaros las herramientas que tenéis:</p>
    '''
    if not parameters.domain:
        myDomain = "vuestro_dominio.com"
    else:
        myDomain = parameters.domain
    message += '''<ul>
    '''
    if parameters.panelRoute:
        message += '''<li> Panel de control en: https://"''' + myDomain + parameters.panelRoute + ''' , donde podréis cambiar contraseñas, crear/borrar usuarias FTP, SSH...
        en base a software libre basado en IspConfig3</li>'''
    if parameters.phpmyadminRoute:
         message += '''<li> Panel de control para la abse de datos: https://"''' + myDomain + parameters.phpmyadminRoute + ''' , donde podréis, con vuestra usuaria establecida en el panel de control para la base de datos
        trabajar sobre esta. Todo en base a software libre basado en PhpmyAdmin</li>'''
    if parameters.webmail:
        message += '''<li> Página web de correo electrónico: https://"''' + myDomain + parameters.webmail + ''' , donde podréis, usar vuestro correo electrónico configurado en el panel de control. 
        Todo en base a software libre basado en Roundcube</li>'''
    if parameters.mailman:
        message += '''<li> Portal de gestión de listas de correo: https://"''' + myDomain + parameters.mailman + ''' , donde podréis, gestionar las listas de correo creadas en el panel de control. 
        Todo en base a software libre basado en Mailman</li>'''
    message += '''
    </ul>'''
    
    return message
