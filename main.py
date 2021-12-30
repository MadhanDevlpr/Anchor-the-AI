import wolframalpha
import sys
import pyttsx3
import wikipedia
import os
import datetime
import speech_recognition as sr  # pip install SpeechRecogniton
import webbrowser  # Pre-Installed Library
name="User"


client = wolframalpha.Client(f'QVU59W-GH87QRUQT8')
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
voices = engine.getProperty(f'voices')
engine.setProperty(f'voice', voices[len(voices)-4].id)
engine. setProperty("volume", 200)


def speak(audio):
    print(f'Anchor: '+audio)
    engine.say(audio)
    engine.runAndWait()

# Welcome the user

def wishMe():
    time = int(datetime.datetime.now().hour)
    if time >= 0 and time < 12:
        speak(f'Good Morning {name}!')

    if time >= 12 and time < 18:
        speak(f'Good Afternoon {name}!')

    if time >= 18 and time !=0:
        speak(f'Good Evening {name}!')



def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f'')
        print("Listening...")
        r.pause_threshold = 1
        hearing = r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f'User: ' + query)
    except:
        speak('I can\'t hear that properly, try typing the command')
        query = input('Enter your command: ')
    return query


# The main code Artificial Intelligence


if __name__ == '__main__':
    wishMe()
    while True:
        command = myCommand().lower()
        if 'google' in command:
            speak(f'Should I search for something?')
            searchDataAnswer = myCommand().lower()
            if 'ye' in searchDataAnswer:
                speak(f'Okay, tell me what to search for')
                searchData = myCommand().lower()
                try:
                    webbrowser.open(f'https://www.google.com/search?q='+searchData)
                except:
                    speak(f'Error searching, trying connecting to your net or see if your microphone works')
            else:
                speak(f'Okay,opening google for you')
                webbrowser.open(f'https://www.google.com/search?q=')
        elif 'close' in command:
            speak(f'See you later {name} ')
            sys.exit()

        elif 'map' in command:
            speak(f'Should I search for the place?')
            searchDataAnswer = myCommand().lower()
            run = True
            while run:
                if 'ye' in searchDataAnswer:
                    speak(f'Okay, tell me what to search for')
                    searchData = myCommand().lower()
                    try:
                        webbrowser.open(f'https://www.google.com/maps/place/'+searchData)
                        run = False

                    except:
                        speak(f'Error searching, trying connecting to your net or see if your microphone works')
                        run = False
                else:
                    speak(f'Okay,opening google maps for you')
                    webbrowser.open(f'https://www.google.com/maps')
                    run=False


        elif ' youtube' in command:
            speak(f'What should I search?')
            video = myCommand().lower()
            try:

                webbrowser.open(f'https://www.youtube.com/results?search_query='+video)
                speak(f'Youtube is opened')
            except:
                speak(f'Sorry, Unable to search on youtube')

        elif ' gmail' in command:
            webbrowser.open(f'https://mail.google.com/mail/u/0/#inbox')
            speak(f'Gmail is opened')

        elif ' canva' in command:
            webbrowser.open(f'https://www.canva.com/')
            speak(f'Canva is opened')

        elif "what is the date" in command:
            speak(f'The date is ' + str(tday.day) + ' {name}!')

        elif "what's the date" in command:
            speak(f'The date is ' + str(tday.day) + ' {name}!')

        elif "what is today's date" in command:
            speak(f'The date is ' + str(tday.day) + ' {name}!')

        elif "what's today's date" in command:
            speak(f'The date is ' + str(tday.day) + ' {name}!')

        elif "what's the month" in command:
            speak(f'The month is ' + str(tday.month) + ' {name}!')

        elif "what is the month" in command:
            speak(f'The month is ' + str(tday.month) + ' {name}!')

        elif 'who are you' in command:
            speak(f'My name is Anchor , I am your Desktop assistant')

        elif 'how are you' in command:
            speak(f'I am fine {name}!')

        elif ' amazon' in command:
            speak(f'What should I search?')
            product = myCommand().lower()
            try:
                webbrowser.open(f'https://www.amazon.in/s?k='+product)
                speak(f'okay!')
            except:
                speak(f'sorry, unable to search')

        elif ' scratch' in command:
            webbrowser.open(f'https://scratch.mit.edu/#')
            speak(f'Scratch is opened')

        elif 'hello' in command:
            speak(f'Hello {name}!')

        elif 'what can you do' in command:
            speak(f'I can control your desktop, and make all voice controlled')

        elif ' disney' in command:
            speak(f'What should I search?')
            movie = myCommand().lower()
            try:
                webbrowser.open(f'https://www.hotstar.com/in/search?q='+movie)
                speak(f'okay!')
            except:
                speak(f'sorry, unable to search!')

        elif ' browser' in command:
            webbrowser.open(f'#')
            speak(f'Browser is opened')

        elif ' command prompt' in command:
            speak(f'Yes {name}')
            os.startfile(f'C:/Windows/System32/cmd.lnk')

        elif ' notepad' in command:
            speak(f'Notepad is opened!')
            os.startfile(f'C:/Users/P {name} AADITHYA/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad.lnk')

        elif ' word' in command:
            os.startfile(f'C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Word.lnk')
            speak(f'Microsoft word is opened!')


        elif "what's the time" in command:
            time()

        elif "what is the time" in command:
            time()

        elif 'search on wikipedia' in command:
            speak(f'Tell me what do you want to search')
            run = True
            while run:

                dataa = myCommand()

                data = wikipedia.summary(dataa)
                speak(f'Accordind to wikipedia,')



                speak(data)
                run = False


        elif 'shutdown' in command:
            closing = True
            speak(f'Do you really need to shutdown?')
            while closing:
                yesorno = myCommand()
                if 'yes' in yesorno.lower():
                    os.system(f'shutdown /s /t 0')
                    sys.exit()
                else:
                    speak("It's a right choice {name}!")
                    closing = False




        else:
            try:
                try:
                    speak(f'Searching...')
                    res = client.query(command)
                    answer = next(res.results).text

                    speak(f'According to the net,')
                    speak(answer)
                except:
                    speak(f'searching for it, {name}')
                    data = wikipedia.summary(command, sentences=2)
                    speak(data)

            except:
                speak(f'No results for it, opening it in google')
                webbrowser.open(f'https://www.google.com/search?q='+command)

# This is fantastic
# This is made by {name} Aadithya
# Started on 5 December 2020
# Finished on 30 December 2021
#____X____#

