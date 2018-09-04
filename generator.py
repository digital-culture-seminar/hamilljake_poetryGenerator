# -*- coding: utf-8 -*-
"""
Author: Jake Hamill
Description: python poen generator
License: GNU General Public License 
August 28, 2018
"""

import random

# list of nouns

nouns = ["sailor", 
         "jawbreaker", 
         "jellyfish", 
         "slurpee"]

# list of verbs

verbs = ["swims", 
         "falls", 
         "monitors", 
         "bursts"]

# list of adjectives

adjectives = ["mysterious", 
              "shriveled", 
              "colossal", 
              "obedient"]

# random + new variable

noun = random.choice(nouns)
verb = random.choice(verbs)
adjective = random.choice(adjectives)

print "The " + adjective + " " + noun + " " + verb + ""

#i = 0
#for verb in verbs:
#    whitespace = " " * i
#    print whitespace + verb
#    i = i + 1
    
#i = 0
#for noun in nouns:
#    whitespace = " " * i
#    print whitespace + noun
#    i = i + 1    
    
    
    


