"""
AUTHOR: Jake Hamill
DESCRIPTION: python text generator
LISCENSE: GNU General Public Liscense v2
"""
import random

#list of nouns
nouns = ["sailor",
         "ship",
         "anchor"]
#list of verbs
verbs = ["sailor",
         "ship",
         "anchor"]

noun = random.choice(nouns)

#two diff ways to print
#print "The " + nouns" + verbs " "+ "."

print "The {n} {v}.".format(n=noun, v=verb)
