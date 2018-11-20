# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:29:16 2018

@author: hamill
"""

# Connect to generated POEM 

#import libs
from playsound import playsound
from gtts import gTTS
import markovify

with open ("NC_LandscapeOrdinance.txt") as file:
    things = file.read()
    
with open ("PhilOfBeauty.txt") as file:
    fog = file.read()
    
with open ("NC_LandscapeOrdinance.txt") as file:
    stars = file.read()
        
direction_model = markovify.Text(things)
horror_model = markovify.Text(fog)
science_model = markovify.Text(stars)

poem = ""

a = 3
b = 2
c = 1
i = 0 
for i in range(0,3):
    a = a - i
    c = c + i
    synthesized_model = markovify.combine([direction_model, horror_model, science_model],[a,b,c])
    poem = poem + synthesized_model.make_sentence()
    
    
#    print "i = " + str(i)
#    print "a = " + str(a)
#    print "c = " + str(c)
    
print poem
    
with open("doc.md", "a") as f:
    f.write("""

```
{poem}
```
""".format(poem=poem))

# build the markov model
text_model = markovify.NewlineText(poem)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(240)
#text_model.make_short_sentence(140)

#text to speech
tts = gTTS(text=poem, lang="en")

#write audio file
tts.save("mp3s/nature_07.mp3")

#play audio file
playsound("mp3s/nature_07.mp3")