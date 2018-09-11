# -*- coding: utf-8 -*-
"""
Author: Jake Hamill
Description: python poen generator
License: GNU General Public License 
August 28, 2018

"""
"""
Inevitability of Change (and question of if a change is powerful enough to keep a system going)


English
A storm bubbles far on the horizon. 
Shapeshifting, always moving closer and farther away
Light pours through holes in thick grey clouds
Glimmering off of houses that perspire through
generations of brightly colored paint.
Paint that keeps these structures 
huffing and puffing bones exhausted
I know that if these houses can get one more layer of paint
then I might just see them once again
standing brilliantly against this wall of grey. 

Russian

(rep) pour light
(with) shed light

(rep)huffing and puffing bones exhausted 
(with) dead and burning

Hindi

(rep) pour light
(with) throw light

(rep) brightly colored paint
(with) shiny colored paint 

(rep) huffing and puffing
(with) laughing at the bones

Japanes

Storms are blew on the horizon.
Shapsifting is a generation of bright colored paint that
is always farther and far away, and is the shaking house
in which light is poured into the hole in a thick gray cloud.
I'm tired of the Painting bone that holds these structures,
and I'm tired of these houses,
and I'm going to see them again, 
and I'm standing on this gray wall, 
and I'm standing on this gray wall.
"""
import random

# list of nouns

nouns = ["sailor", 
         "jawbreaker", 
         "jellyfish", 
         "slurpee"]

# list of verbs

verbs = ["swims", 
         "tumbles", 
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
    
    
    


