# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:13 2018

@author: hamil
"""

import markovify

with open ("1000things.txt") as thingstoknow:
    things = thingstoknow.read()
    
with open ("ghost.txt") as superghost:
    markovghost = superghost.read()
    
things_model = markovify.Text(things)
ghost_model = markovify.Text(markovghost)
combo_model = markovify.combine([things_model, ghost_model], [1.2,1])

#print combo_model.make_sentence()    

for i in range(3):
    print combo_model.make_sentence()
    print" "

    
