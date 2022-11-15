# Requirements

  # 
    import speech_recognition as sr #to listen 
    import pyttsx3                  #to convert text to speech  
    import pywhatkit                #to play youtube video etc
    import datetime                 #take get date and time
    import wikipedia                # to get information from wikkipedia 
    import pyjokes                  # to get jokes 
    import webbrowser               # to open any website

# step 1 Listening and recognize

      import speech_recognition as sr

      #create listener to recognize your voice 
      listener = sr.Recognizer()          

      #use microphone as source and call sr to listen the source 
          try:
              with sr.Microphone() as source:                               
                  print('listening...')
                  voice = listener.listen(source)
                  command = listener.recognize_google(voice)  #take voice or input
                  command = command.lower()
                  if 'Toodles' in command:                # if 'toodles' is present ignore it 
                      command = command.replace('Toodles', '')
                      print(command)
          except:
              print('use microphone or make sure speak properly')  #if u dont speak anything  

# step 2 conversion of text to speech

    import pyttsx3
    #converting texts into speech 
    engine = pyttsx3.init()
    def talk(text):
        engine.say(text)
        engine.runAndWait()      

# step 3 taking command and giving results

      import pywhatkit
      import datetime
      import wikipedia
      import pyjokes
      import webbrowser

      def run_toodles():
          command = take_command()
          print(command) 

          # if play is present it opens youtube play song
          if 'play' in command:   
              song = command.replace('play', '')
              talk('playing ' + song)
              pywhatkit.playonyt(song)

         #if time is prsent it gives time and date
          elif 'time' in command:
              time = datetime.datetime.now().strftime('%I:%M %p')
              talk('Current time is ' + time)
              print(time)

           # if who is present it gives info of that person 
          elif 'who is'  in command:
              person = command.replace('who is', '')
              info = wikipedia.summary(person, 1) #get 1st 2 lines from wikki
              print(info)
              talk(info)

          #create your own question and ans
          elif 'single' in command:
              talk(' i have a boyfriend  ')
          elif 'boyfriend' in command:
              talk('my boyfriend name is tom')

           # if joke is present it tells joke 
          elif 'joke' in command:
              talk(pyjokes.get_joke())
              print(pyjokes.get_joke())

          # open chrome , facebook etc
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

          # if u ask something rather then above 
          else:
              talk('Please say the command again.')

      run_toodles()

# snapshots 

# time
![image](https://user-images.githubusercontent.com/105975325/201854304-6d86866b-569a-4890-b33a-a569b73b9572.png)


# getting info from wikkipedia 
![image](https://user-images.githubusercontent.com/105975325/201853512-2e6d06f3-9eff-47f6-8c3a-d7f2ecd4a53b.png)

# asking joke
![image](https://user-images.githubusercontent.com/105975325/201853571-0d1c128d-5301-4973-8009-ff9db2a30873.png)






