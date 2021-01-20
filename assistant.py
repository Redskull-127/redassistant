import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

speak("Welcome Redskull")
def speak(tex):
	tts = gTTS(text=tex, lang="en")
	filename = "voicee.mp3"
	tts.save(filename)
	playsound.playsound(filename)


speak("Enter Your Password")
g = input("Enter Your Password : ")
if g == '3690':
	def speak(granted):
		tts = gTTS(text=granted, lang="en")
		filename = "granted.mp3"
		tts.save(filename)
		playsound.playsound(filename)
	speak("Password Granted. Creating Environment")
else:
	print("Fuck Off")
	def speak(fuck):
		tts = gTTS(text=fuck, lang="en")
		filename = "fuck.mp3"
		tts.save(filename)
		playsound.playsound(filename)
	speak("Fuck Off")
 