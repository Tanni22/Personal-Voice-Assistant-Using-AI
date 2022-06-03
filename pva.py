import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from time import ctime
import time
import webbrowser
from gtts import gTTS
import os
import ctypes
import smtplib
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
     
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Good Morning!")
    elif hour>=12 and hour<18:
         speak("Good Afternoon!")   
    else:
         speak("Good Evening!") 

    speak("I am your personal Assistant. Please tell me how may I help you")

def send_email(to,content):
     server=smtplib.SMTP("smtp.gmail.com",587)
     server.ehlo()
     server.starttls()

     server.login("kaniztanni22@gmail.com","Tanni@200022@$")
     server.sendmail("kaniztanni22@gmail.com",to,content)
     server.close()

def takecommand():
     r=sr.Recognizer()
     with sr.Microphone() as source:
          print("Listening...")
         
          r.pause_threshold=1
          r.adjust_for_ambient_noise(source, 1)
          audio=r.listen(source)
     
     try:
          print("Recognizing...")
         
          query=r.recognize_google(audio,language='en-in')
          print(f"User said: {query}\n")
           
     except Exception as e:
          print(e)

          print("Say that again please...")
          return "None"
     return query

if __name__=="__main__":
    wishme()
    while True:
   
        query = takecommand().lower()

        if query in (["how are you","how are you doing"]) :
           speak("I'm very well, thanks for asking ")

    
        if query in (["what is the time","tell me the time","what time is it"]):
            import datetime
            now = datetime.datetime.now()
            h=now.hour
            m=now.minute
            speak('Current time is %d hours %d minutes' % (now.hour, now.minute))
            print('Current time is %d hours %d minutes' % (now.hour, now.minute))
        
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif ' youtube' in query:
             search_term= query.split("for")[-1]
             url = "https://www.youtube.com/results?search_query=" + search_term
             webbrowser.get().open(url)
             speak("Here is what I found for " + search_term + "on youtube")
       
        elif 'facebook' in query:
             search_term= query.split("for")[-1]
             url = "https://www.facebook.com/" 
             webbrowser.get().open(url)
             speak("Opening facebook")
        
        elif 'whatsapp' in query:
             search_term= query.split("for")[-1]
             url = "https://www.whatsapp.com/" 
             webbrowser.get().open(url)
             speak("Opening whatsapp")
       
        elif 'instagram' in query:
             search_term= query.split("for")[-1]
             url = "https://www.instagram.com/" 
             webbrowser.get().open(url)
             speak("Opening instagram")
        
        elif 'play music' in query:
            search_term= query.split("for")[-1]
            url="https://open.spotify.com/search/"+search_term
            webbrowser.get().open(url)
            speak("You are listening to"+ search_term +"enjoy sir")

        elif 'search' in query:
            search_term= query.split("for")[-1]
            url="https://www.google.com/search?q=/"+search_term
            webbrowser.get().open(url)
            speak("You are searching"+ search_term +"on google")
        
        elif 'where is' in query:
             search_term= query.split("for")[-1]
             url="https://www.google.com/maps/place/" +  search_term
             webbrowser.get().open(url)
             speak("This is where" + search_term + "is.")

        elif query in (["weather","how the weather outside","Please get the report of waether"]):
             search_term=query.split("for")[-1]
             url="https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
             webbrowser.get().open(url)#opens the webrowser
             speak("Here is your report ")

        elif 'open VS' in query:
              codePath ="C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
              os.startfile(codePath)
              speak("Opening Visual studio")

        elif 'mail' in query:
              try:
                  speak("What should i say?")
                  content=takecommand()
                  speak("whom should i send")
                  to=input("Enter the email address: ")
                  send_email(to,content)
                  speak("Email has been send")
              except Exception as e:
                   print(e)
                   speak("I am not avail to send this email")

        elif  query in (["exit","goodbye","quit","take some rest bro"]):
              speak("We could continue more, well goodbye")
              exit()

        
           
       