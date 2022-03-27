import sys
import webbrowser

import speech_recognition as sr
import pyttsx3
# import pyjokes
import os
import datetime
# import wikipedia
import multiprocessing
import playsound
from gtts import gTTS
import os
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
