import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            talk('hi tom')
            talk('how can i help you')
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Toodles' in command:
                command = command.replace('Toodles', '')
                print(command)
            

    except:
        print('use microphone or make sure speak properly')
    return command


def run_toodles():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
    elif 'who is'  in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'single' in command:
        talk(' i have a boyfriend  ')
    elif 'boyfriend' in command:
        talk('my boyfriend name is tom')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        talk(pyjokes.get_joke())

    elif 'chrome' in command:
        talk('opening chrome')
        webbrowser.open_new("www.google.com")
    elif 'facebook' in command:
        talk('opening facebook')
        webbrowser.open_new('www.facebook.com')
    elif 'weather' in command:
        talk('opening weather report')
        webbrowser.open_new("https://www.bbc.com/weather/1277333")
    elif 'map' in command:
        talk('opening google map')
        webbrowser.open_new("https://www.google.com/maps")

    else:
        talk('Please say the command again.')

run_toodles()


