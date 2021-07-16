import wolframalpha
import sys
import pyttsx3
import wikipedia
import os
import datetime
import speech_recognition as sr  # pip install SpeechRecogniton
import webbrowser  # Pre-Installed Library



client = wolframalpha.Client('QVU59W-GH87QRUQT8')
Time = datetime.datetime.now().strftime("%H:%M:%S")
hours = datetime.datetime.now().strftime("%H")
minutes = datetime.datetime.now().strftime("%M")
seconds = datetime.datetime.now().strftime("%S")


def time():
    hours = datetime.datetime.now().strftime("%H")
    hour = int(hours) - 12
    minutes = datetime.datetime.now().strftime("%M")
    seconds = datetime.datetime.now().strftime("%S")
    speak("It's " + str(hour)+' hours and '+str(minutes)+' minutes and '+str(seconds)+' seconds'  )

# Speech Recogniton variables
recorder = sr.Recognizer()
mic = sr.Microphone()
# Time variable
tday = datetime.date.today()
# Initializing speak function
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-4].id)


def speak(audio):
    print('Jarvis: '+audio)
    engine.say(audio)
    engine.runAndWait()

# Welcome the user

def wishMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak('Good Morning Master!')

    if time >= 12 and time < 18:
        speak('Good Afternoon Master!')

    if time >= 18 and time !=0:
        speak('Good Evening Master!')



def myCommand():



    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('')
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query)


    except:
        speak("Sorry about that, I didn't hear that properly , Try typing the command")
        query = str(input('Command: '))
    return query


# The main code Artificial Intelligence


if __name__ == '__main__':
    wishMe()
    while True:
        command = myCommand().lower()
        if 'open google' in command or 'search on google' in command:
            speak('Okay')
            webbrowser.open('https://www.google.com.tw/?#q=')
        elif 'close' in command:
            speak('See you later Master ')
            sys.exit()

        elif 'open map' in command:
            speak('What should I search?')
            run = True
            while run:
                location = myCommand().lower()
                try:
                    webbrowser.open('https://www.google.com/maps/place/'+location)
                    run = False
                except:
                    speak('Sorry, Unable to search')
                    run = False


        elif 'open youtube' in command:
            speak('What should I search?')
            video = myCommand().lower()
            try:

                webbrowser.open('https://www.youtube.com/results?search_query='+video)
                speak('Youtube is opened')
            except:
                speak('Sorry, Unable to search on youtube')

        elif 'open gmail' in command:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
            speak('Gmail is opened')

        elif 'open canva' in command:
            webbrowser.open('https://www.canva.com/')
            speak('Canva is opened')

        elif "what is the date" in command:
            speak('The date is ' + str(tday.day) + ' master!')

        elif "what's the date" in command:
            speak('The date is ' + str(tday.day) + ' master!')

        elif "what is today's date" in command:
            speak('The date is ' + str(tday.day) + ' master!')

        elif "what's today's date" in command:
            speak('The date is ' + str(tday.day) + ' master!')

        elif "what's the month" in command:
            speak('The month is ' + str(tday.month) + ' master!')

        elif "what is the month" in command:
            speak('The month is ' + str(tday.month) + ' master!')

        elif 'who are you' in command:
            speak('My name is Jarvis , I am your Desktop assistant')

        elif 'how are you' in command:
            speak('I am fine Master!')

        elif 'open amazon' in command:
            speak('What should I search?')
            product = myCommand().lower()
            try:
                webbrowser.open('https://www.amazon.in/s?k='+product)
                speak('okay!')
            except:
                speak('sorry, unable to search')

        elif 'open scratch' in command:
            webbrowser.open('https://scratch.mit.edu/#')
            speak('Scratch is opened')

        elif 'hello' in command:
            speak('Hello Master!')

        elif 'what can you do' in command:
            speak('I can control your desktop, and make all voice controlled')

        elif 'open disney' in command:
            speak('What should I search?')
            movie = myCommand().lower()
            try:
                webbrowser.open('https://www.hotstar.com/in/search?q='+movie)
                speak('okay!')
            except:
                speak('sorry, unable to search!')

        elif 'open browser' in command:
            webbrowser.open('https://www.google.com.tw/?#q=')
            speak('Browser is opened')

        elif 'open hindu' in command:
            webbrowser.open('https://ywc.thehindu.com/junior/')
            speak('Young world is opened')

        elif 'open whatsapp' in command:
            speak('Yes master')
            os.startfile("E:/Whatsapp.lnk")

        elif 'open my books' in command:
            speak('Yes master')
            os.startfile('C:/Users/P MADHAN AADITHYA/OneDrive/Desktop/VII CBSE')

        elif 'open command prompt' in command:
            speak('Yes Master')
            os.startfile('C:/Windows/System32/cmd.lnk')

        elif 'open notepad' in command:
            speak('Notepad is opened!')
            os.startfile('C:/Users/P MADHAN AADITHYA/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad.lnk')

        elif 'open word' in command:
            os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk')
            speak('Microsoft word is opened!')

        elif 'open my projects' in command:
            os.startfile('E:/PycharmProjects')
            speak('I have opened your projects, Master!')

        elif "what's the time" in command:
            time()

        elif "what is the time" in command:
            time()

        elif 'search on wikipedia' in command:
            speak('Tell me what do you want to search')
            run = True
            while run:

                dataa = myCommand()

                data = wikipedia.summary(dataa)
                speak('Accordind to wikipedia,')



                speak(data)
                run = False

        elif 'play music' in command:
            os.startfile('C:/Users/P MADHAN AADITHYA/Music/Video Projects/M.mp3' or 'C:/Users/P MADHAN AADITHYA/Music/Video Projects/A.mp3')
            speak("Here is your music , Master")

        elif 'play master song' in command:
            speak('Yes Master!')
            webbrowser.open('https://www.youtube.com/watch?v=fRD_3vJagxk')

        elif 'play game' in command:
            speak('Okay!')
            os.startfile('E:/PycharmProjects/Games/Pingpong.py')

        elif 'shutdown' in command:
            closing = True
            speak('Do you really need to shutdown?')
            while closing:
                yesorno = myCommand()
                if 'yes' in yesorno.lower():
                    speak('Have a good day!, Master!')
                    os.system('shutdown /s /t 0')
                    sys.exit()
                else:
                    speak("It's a right choice Master!")
                    closing = False




        else:
            try:
                try:
                    speak('Searching...')
                    res = client.query(command)
                    answer = next(res.results).text

                    speak('According to the net,')
                    speak(answer)
                except:
                    speak('According to wikipedia')
                    data = wikipedia.summary(command, sentences=2)
                    speak(data)

            except:
                webbrowser.open('https://www.google.com.tw/?#q='+command)

# This is fantastic
# This is made by Madhan Aadithya
# Started on 5 December 2020
# Finished on 6 February 2021
#____X____#

