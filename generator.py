# -*- coding: utf-8 -*-
"""
Author: Jake Hamill
Description: python poen generator
License: GNU General Public License 
August 28, 2018

"""
"""
Artist Statement
This poem is about the inevitability of change (and the question of if a 
change is powerful enough to completely change a system rather than 
dress it up as different)


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
standing brilliantly against this wall of gray. 

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

Japanese

Storms are blew on the horizon.
Shapsifting is a generation of bright colored paint that
is always farther and far away, and is the shaking house
in which light is poured into the hole in a thick gray cloud.
I'm tired of the Painting bone that holds these structures,
and I'm tired of these houses,
and I'm going to see them again, 
and I'm standing on this gray wall, 
and I'm standing on this gray wall.

Korean

The storm bubbles in the horizon.
It's always a transformation and a distant transformation.
Light is poured out through the holes of thick grey clouds.
The twinkling of a hard house.
The generation of bright-colored paint
Paint Maintaining This Structure
Burnout and bone are bloat.
If we paint the houses one more time,
Then I may look at them once again.
This gray wall is standing well.
"""
import random

# list of nouns

poems = ["The storm bubbles on the horizon. It's always a transformation. "
         "It's always a transformation and a distant transformation. "
         "Light is poured out through holes in the thick grey clouds. "
         "The twinkling of a hard house. The generation of bright colored paint. "
         "Paint maintaining this structure burnout with bloated bones. " 
         "If we paint the house one more time then I may look at it once again. "
         "This grey wall is standing well.", "Storms are blowing on the horizon. "
         "Shapeshifting is a generation of bright colored paint that is always farther and far away, "
         "and is the shaking house in which light is poured into the hole in a thick grey cloud. "
         "I'm tired of the painted bone that holds these structures, and I'm tired of these houses, "
         "but I'm going to see them again, and I'm standing on this grey wall, "
         "and I'm standing on this grey wall. "]


# list of verbs

#verbs = ["swims", 
#         "tumbles", 
#         "monitors", 
#         "bursts"]

# list of adjectives

#adjectives = ["mysterious", 
#              "shriveled", 
#              "colossal", 
#              "obedient"]

# random + new variable

poem = random.choice(poems)
#verb = random.choice(verbs)
#adjective = random.choice(adjectives)

print poem

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
    
    
    


