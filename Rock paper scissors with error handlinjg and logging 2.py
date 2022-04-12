# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 15:23:34 2019

@author: jaredalbert
"""
import re
import logbook
import sys

level = logbook.TRACE
log_filename = 'logout.log'

if not log_filename:
    logbook.StreamHandler(sys.stout, level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(
            log_filename, level=level, date_format='%Y-%m-%d'
            ).push_application()


movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')
#print(movies)
for movie in movies:
    ret_val = re.findall(r'\w+', movie)
    trimmed = ret_val[1:-1]
    if len(trimmed)==2:
        string_trimmed = ' '.join(str(e) for e in trimmed)
        print(string_trimmed, len(trimmed))

#ret_val =  re.findall(r'\D+', movies)
#print(ret_val, len(ret_val))