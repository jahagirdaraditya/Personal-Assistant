from tkinter import *
from PIL import ImageTk, Image
import image
import speech_recognition as sr
import pyttsx3
import datetime
import sys
import wikipedia
import wolframalpha
import os
import smtplib
import random
import webbrowser
import pygame
import subprocess
import pyaudio
import cv2
from gtts import gTTS

client = wolframalpha.Client('G498JW-42JPGTK9Y8')

folder = 'F:/Downloads/Song/'
path = 'E:/Python/Assistant/'
            
engine = pyttsx3.init()
voices = engine.getProperty('voices')

b_music = ['CoolMusic']
pygame.mixer.init()
pygame.mixer.music.load(folder + random.choice(b_music) + '.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

def speak(audio):
    print('Assistant :', audio)
    engine.setProperty('voice', voices[len(voices) - 1].id)
    engine.say(audio)
    engine.runAndWait()

def myCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:                                         
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Try again')
        pass

    return query


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

class Widget:
    def __init__(self):
       root = Tk()
       root.title('Digital Personal Assistant')
       root.config(background='Red')
       root.geometry('350x600')
       root.resizable(0,0)
       root.iconbitmap(r'E:/Python/Assistant/Capture.ico')
       img = ImageTk.PhotoImage(Image.open(r"E:/Python/Assistant/Back.jpg"))
       panel = Label(root, image = img)
       panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="USER", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
       left2.config(font=("Comic Sans MS", 10, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="ASSISTANT", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='Red',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white', command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white', command=root.destroy).pack(fill='x', expand='no')

       
       speak('Hello, I am your digital Personal Assistant! What should I do for You?')
       self.compText.set('Hello, I am your digital Personal Assistant! What should I do for You?')

       root.bind("<Return>", self.clicked) 
       root.mainloop()
    
    def clicked(self):
        #while True:
        print('Working')
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()

        if 'open google chrome' in query:
            self.compText.set('okay')
            speak('okay')
            #subprocess.call(r'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
            os.system("start notepad.exe")

        elif 'kill chrome' in query or 'close chrome' in query or 'close google chrome' in query or 'kill google chrome' in query:
    		# if query == 'kill notepad':
                print("Now I'm killing all running chrome")
                result=os.system("taskkill /im chrome.exe /f")
                # process result
                if result == 0:
                        print("All nodepads should be death now...")
                else:
                        print("Error executing taskkill command !!!")
        
        elif 'open notepad' in query:
            self.compText.set('okay')
            speak('okay')
            #subprocess.call(r'C:/Windows/NOTEPAD.EXE')
            os.system("start notepad.exe")

        elif 'kill notepad' in query or 'close notepad' in query:
    		# if query == 'kill notepad':
                print("Now I'm killing all running notepads")
                result=os.system("taskkill /im notepad.exe /f")
                # process result
                if result == 0:
                        print("All nodepads should be death now...")
                else:
                        print("Error executing taskkill command !!!")

        elif 'click the photo' in query or 'click the pic' in query:
            speak('Okay!')
            speak('Smile Please!')
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite('Pic'+'.png', image)
            #cv2.imshow('Pic'+'.png', image)
            #cv2.imshow("Image", image)
            del(camera)

        elif 'open excel' in query:
            self.compText.set('okay')
            speak('okay')
            #subprocess.call(r'C:/Program Files (x86)/Microsoft Office/Office16/EXCEL.EXE')
            os.system("start excel.exe")

        elif 'kill excel' in query or 'close excel' in query:
    		# if query == 'kill notepad':
                print("Now I'm killing all running excels")
                result=os.system("taskkill /im excel.exe /f")
                # process result
                if result == 0:
                        print("All excels should be death now...")
                else:
                        print("Error executing taskkill command !!!")

        elif 'open youtube' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open flipkart' in query or 'open Flipkart' in query or 'open FlipKart' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.flipkart.com')

        elif 'open google' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'thank you' in query or 'thanks' in query:
            speak('Welcome sir')
            speak('Its my pleasure')

        elif 'love you' in query or 'i love you' in query or 'good job' in query or 'great job' in query:
            speak('Thank you sir')
            #speak('Its my pleasure')    

        elif 'hate you' in query or 'i hate you' in query or 'go to hell' in query:
            speak('whats wrong by me sir?')    

        elif 'open gmail' in query:
            self.compText.set('okay')
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'shutdown' in query:
            self.compText.set('okay')
            speak('okay')
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            self.compText.set(random.choice(stMsgs))
            speak(random.choice(stMsgs))

        elif 'email' in query or 'send email' in query or 'send mail' in query or 'mail' in query:
            self.compText.set('Who is the recipient? ')
            speak('Who is the recipient? ')
            recipient = myCommand()
            self.userText.set(recipient)
            recipient = recipient.lower()

            if 'me' in recipient or 'ME' in recipient or 'mi' in recipient or 'MI' in recipient:
                try:
                    self.compText.set('What should I say? ')
                    speak('What should I say? ')
                    content = myCommand()
                    self.userText.set(content)
        
                    server = smtplib.SMTP('smtp.gmail.com',587)
                    server.ehlo()
                    server.starttls()
                    server.login("s16_jahagirdar_aditya@mgmcen.ac.in", 'Your_Password')
                    server.sendmail('s16_jahagirdar_aditya@mgmcen.ac.in', "aditya.jahagirdar05@yahoo.com", content)
                    server.close()
                    self.compText.set('Email sent!')
                    speak('Email sent!')

                except:
                    self.compText.set('Email sent!')
                    speak('Sorry ' + 'Sir' + '!, I am unable to send your message at this moment!')



        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            self.compText.set('Okay')
            speak('okay')
            #self.compText.set('Bye Sir, have a good day.')
            #speak('Bye Sir, have a good day.')
           
        elif 'hello' in query or 'hi' in query or 'Hello' in query or 'Hi' in query:
            self.compText.set('Hello Sir/Madam...')
            #speak('Hello Sir/Madam...')
            speak('Hello Everyone...')

        elif 'bye' in query:
            self.compText.set('Bye Sir have a good day.....')
            speak('Bye Sir have a good day.....')
            exit()
                                    
        elif 'play music' in query:
            music_folder = 'D:/Songs/Sg/'
            music = ['JabTak', 'Bandeyaa', 'EkMulaqat', 'TereSang', 'Rabba']
            random_music = music_folder + random.choice(music) + '.mp3'
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')
            os.system(random_music)
                        
        elif 'play movie' in query or 'play video' in query:
            music_folder = 'D:/Movies/New/'
            music = ['LUKACHUPI']
            random_music = music_folder + random.choice(music) + '.mkv'
            os.system(random_music)
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')
        
        elif 'make audio' in query:
            #path = 'E:/Python/Assistant/'
            #music = ['welcome']
            mytext = str(input('Enter text to make audio : '))
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False) 
            myobj.save("welcome.mp3")
            music = path + 'welcome.mp3'
            self.compText.set('Okay, here is your music! Enjoy!')
            speak('Okay, here is your music! Enjoy!')
            os.system(music)
            
        elif 'show photo' in query or 'show pic' in query:
            #path = 'E:/Python/Assistant/'
            #music = ['welcome']
            #mytext = str(input('Enter text to make audio : '))
            #language = 'en'
            #myobj = gTTS(text=mytext, lang=language, slow=False) 
            #myobj.save("welcome.mp3")
            photo = path + 'Pic.jpg'
            self.compText.set('Okay, here is your photo! Enjoy!')
            speak('Okay, here is your photo! Enjoy!')
            os.system(photo)
        
        else:
            query = query
            speak('Searching on the internet...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('I got it...')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('I got it on internet and it says :-')
                    
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        

if __name__ == '__main__':
    greetMe()
    widget = Widget()
