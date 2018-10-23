# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 18:29:16 2018

@author: hamil
"""

# Connect to generated POEM 

#import libs
from playsound import playsound
from gtts import gTTS
import markovify

with open ("storm.txt") as file:
    things = file.read()
    
with open ("storm.txt") as file:
    fog = file.read()
    
with open ("storm.txt") as file:
    stars = file.read()
        
direction_model = markovify.Text(things)
horror_model = markovify.Text(fog)
science_model = markovify.Text(stars)


synthesized_model = markovify.combine([direction_model, horror_model, science_model],[1,1,1])

  
poem = synthesized_model.make_sentence() + synthesized_model.make_sentence()

    
with open("doc.md", "a") as f:
    f.write("""

```
{poem}
```
""".format(poem=poem))

# build the markov model
text_model = markovify.NewlineText(poem)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(140)
#text_model.make_short_sentence(140)

#text to speech
tts = gTTS(text=poem, lang="en")

#write audio file
tts.save("mp3s/purpose84.mp3")

#play audio file
playsound("mp3s/purpose84.mp3")