import wolframalpha
import sys
import pyttsx3
import wikipedia
import os
import pyautogui
import datetime
import time as ts
import pywhatkit
import speech_recognition as sr  # pip install SpeechRecogniton
import webbrowser  # Pre-Installed Library


dbfile = open("db.txt","r")
Counter = 0
  
# Reading from file
Content = dbfile.read()
CoList = Content.split("\n")
  
for i in CoList:
    if i:
        Counter += 1


if Counter == 0:
    name=input('Enter the name which has to be callen by me: ')
    dbfile = open("db.txt","w")
    dbfile.write(name)
    dbfile.close()
else:
    dbfile = open("db.txt","r")
    name = dbfile.read()



client = wolframalpha.Client(f'QVU59W-GH87QRUQT8')
Time = datetime.datetime.now().strftime("%H:%M:%S")
hours = datetime.datetime.now().strftime("%H")
minutes = datetime.datetime.now().strftime("%M")
seconds = datetime.datetime.now().strftime("%S")


def time():
    hour = int(hours) - 12
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
        speak('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User: ' + query)
    except:
        query = "_"
        
    return query


# The main code Artificial Intelligence


if __name__ == '__main__':
    print('''
                                      __
                                     /  \ 
                                    / /\ \ 
                                   / /  \ \ 
                                  / /    \ \ 
                                 / /      \ \ 
                                / /        \ \ 
                               / /          \ \ 
                              / /            \ \ 
                             / /              \ \ 
                            / /                \ \ 
                           / /__________________\ \ 
                          / /____________________\ \ 
                         / /                      \ \ 
                        / /                        \ \ 
                       / /                          \ \ 
                      / /                            \ \ 
                     /_/                              \_\ 
    ''')
    wishMe()

    while True:
        command = myCommand().lower()
        if command == "_":
            speak('I can\'t hear it properly, can you please say it again')
            pass

        elif 'anchor' in command:
            speak('I\'m back to service!')
            while True:
                command = myCommand().lower()
                if command == "_":
                    speak('I can\'t hear it properly, can you please say it again')
                    continue

                elif 'change my name' in command:
                    speak('Okay!')
                    new_name = input('Enter your name: ')
                    dbfile = open('db.txt','w')
                    dbfile.write(new_name)
                    dbfile.close()
                    speak('Please restart this application for the update.')

                elif 'take a break' in command:
                    speak(f'Okay,{name}. Just say \'anchor\' to call me.')
                    break

                elif 'press enter' in command:
                    speak(f'Okay {name}')
                    pyautogui.press('enter')
                
                elif 'press space' in command:
                    speak(f'Okay {name}')
                    pyautogui.press('space')

                elif 'open google' in command:
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
                    break

                elif 'open map' in command:
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


                elif 'open youtube' in command:
                    speak(f'What should I search?')
                    video = myCommand().lower()
                    try:

                        webbrowser.open(f'https://www.youtube.com/results?search_query='+video)
                        speak(f'Youtube is opened')
                    except:
                        speak(f'Sorry, Unable to search on youtube')

                elif 'play video' in command:
                    speak('Okay, tell me what video to play.')
                    videoName = myCommand().lower()
                    speak(f'Opening {videoName}.')
                    pywhatkit.playonyt(videoName)

                elif 'open gmail' in command:
                    webbrowser.open(f'https://mail.google.com/mail/u/0/#inbox')
                    speak(f'Gmail is opened')

                elif 'open canva' in command:
                    webbrowser.open(f'https://www.canva.com/')
                    speak(f'Canva is opened')

                elif 'right click' in command:
                    speak(f'Okay {name}')
                    pyautogui.rightClick()

                elif 'left click' in command:
                    speak(f'Okay {name}')
                    pyautogui.click()

                elif 'double click' in command:
                    speak(f'Okay {name}')
                    pyautogui.doubleClick()

                elif 'open task manager' in command:
                    speak(f"okay {name}")
                    pyautogui.hotkey('ctrl','shift','esc')


                elif 'open settings' in command:
                    speak(f"Okay {name}")
                    pyautogui.hotkey('win','i')

                elif 'increase volume' in command:
                    speak(f'okay {name}')
                    pyautogui.press('volumeup')

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
                    speak(f'I am fine, {name}!')

                elif 'open amazon' in command:
                    speak(f'What should I search?')
                    product = myCommand().lower()
                    try:
                        webbrowser.open(f'https://www.amazon.in/s?k='+product)
                        speak(f'okay!')
                    except:
                        speak(f'sorry, unable to search')


                elif 'hello' in command:
                    speak(f'Hello {name}!')

                elif 'what can you do' in command:
                    speak(f'I can control your desktop, and make all voice controlled')

                elif 'open disney' in command:
                    speak(f'Should I search for something?')
                    yesorno = myCommand().lower()
                    if 'yes' or 'yeah' or 'sure' in yesorno:
                        movie = myCommand().lower()
                        try:
                            webbrowser.open(f'https://www.hotstar.com/in/search?q='+movie)
                            speak(f'okay!')
                        except:
                            speak(f'sorry, unable to search!')
                    else:
                        webbrowser.open('https://www.hotstar.com/in')

                elif 'open browser' in command:
                    webbrowser.open('https://google.com')
                    ts.sleep(10)
                    pyautogui.press('browsersearch')
                    pyautogui.write('Your browser is opened by AnchorYour browser is opened by Anchor')
                    speak(f'Browser is opened')

                elif 'open command prompt' in command:
                    speak(f'Yes {name}')
                    os.startfile(f'C:/Windows/System32/cmd.lnk')

                elif 'open notepad' in command:
                    speak(f'Notepad is opened!')
                    os.startfile(f'C:/Users/P {name} AADITHYA/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Accessories/Notepad.lnk')

                elif 'open word' in command:
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
                        speak(f'According to wikipedia,')



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
                            speak(f"It's a right choice {name}!")
                            closing = False




                else:
                    try:
                        try:
                            res = client.query(command)
                            answer = next(res.results).text
                            speak(answer)
                        except:
                            speak(f'searching for it, {name}')
                            data = wikipedia.summary(command, sentences=2)
                            speak(data)

                    except:
                        speak(f'No results for it, opening it in google')
                        pywhatkit.search(command)
        else:
            speak(f'I\'m in a break, please say \'anchor\' to wake me up.')



