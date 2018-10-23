# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:13 2018

@author: hamil
"""
#import libs
import markovify
from playsound import playsound
from gtts import gTTS

with open ("1000things.txt") as thingstoknow:
    things = thingstoknow.read()
    
with open ("universe.txt") as superghost:
    markovghost = superghost.read()
    
# build the markov model
text_model = markovify.NewlineText(markovghost)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(140)

#text to speech
tts = gTTS(text=markov_poem, lang="en")

#write audio file
tts.save("../mp3s/mark04.mp3")

#play audio file
playsound("../mp3s/mark04.mp3")







#print
#print combo_model.make_sentence()    

#for i in range(3):
#    print combo_model.make_sentence()
#    print" "

    
