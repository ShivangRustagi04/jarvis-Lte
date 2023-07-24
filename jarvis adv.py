import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import wikipedia
import os
import smtplib
import pygame
import pyautogui
import keyboard
 
Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
print(voices)
Assistant.setProperty("voices",voices[0].id)
Assistant.setProperty("rate",150)
def speak(audio):
    print("   ")
    Assistant.say(audio)
    Assistant.runAndWait()


# if "hello" in query:
#     speak("hello sir")

# else:
#     speak("no command found")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivangrustagi04@gmail.com', 'Laxminagar$92')
    server.sendmail('shivangrustagi04@gmail.com', to, content)
    server.close()


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pygame
import pywhatkit 
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('shivangrustagi04@gmail.com', 'Laxminagar$92')
    server.sendmail('shivangrustagi04@gmail.com', to, content)
    server.close()


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def main():
    def music():
        speak("tell me your music name")
        musicname = takeCommand()
        pywhatkit.playonyt(musicname)
        speak("your music is playing , enjoy it")
    def whatsapp():
        speak("tell me the name of person")
        name = takeCommand()

        if "shlok" in name:
            speak("tell me the message!!")
            msg = takeCommand()
            speak("tell me time in hour and minute")
            hour = int(takeCommand())
            min = int(takeCommand())
            pywhatkit.sendWhatmsg("+919899755982", msg , hour, min , 20)
            speak("ook sir your message will be send!!")   
    def youtubeAuto():
        speak("what is your command")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press("space bar")

        elif "restart" in comm:
            keyboard.press("0")
        elif "mute" in comm:
            keyboard.press("m")
        elif "back" in comm :
            keyboard.press("j")
        elif "skip" in comm :
            keyboard.press("l")
        elif "full screen" in comm :
            keyboard.press("f")
        elif "exit full screen" in comm :
            keyboard.press("f")
        elif "film mode" in comm :
            keyboard.press("t")
        speak("done sir")



    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if "hello" in query:
            speak("hello sir, i am jarvis ")
            speak("i am your ai assistant")
            speak("how can i help you ")
        elif "how are you " in query:
            speak(" i am fine sir thank you for asking")
        
        elif "bye"in query:
            speak("have a good day ahead")
            break
        elif "kya hal hai" in query:
            speak("sab jhakaas hai")
        elif "main achcha hun tum batao" in query:
            speak("main bhi")
        elif "you need break" in query:
            speak("arlight you can call me anytime")
            break
        elif "youtube search" in query:
            speak("ok sir , finding")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = "https://www.youtube.com/results?search_query="  + query
            webbrowser.open(web)
            speak("this is what i found")
        elif "google search" in query:
            speak("okay sir finding")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            speak("DONE sir")
        elif "music" in query:
            music()
        elif "whatsapp" in query:
            whatsapp()
        elif "website" in query:
            speak("ok sir , launching....")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            speak("launched")
        elif "launch" in query:
            speak("ok launching the website you said")
            name = takeCommand()
            web = "https://www." + name +".com"
            webbrowser.open(web)
            speak("done sir")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("this is what i found on internet")
            pywhatkit.search(query)


            try:
                result = googleScrap.summary(query,2)
                speak(result)
            
            except:
                speak("no data found to tell")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_file = 'C:\\Users\\shiva\\Downloads\\music.mp3'  # Replace with the path to your music file
            speak("Playing music now...")
            play_music(music_file)
            while pygame.mixer.music.get_busy():
                continue
            speak("Music has finished playing")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "restart" in query:
            keyboard.press("0")
        elif "mute" in query:
            keyboard.press("m")
        elif "back" in query :
            keyboard.press("j")
        elif "skip" in query :
            keyboard.press("l")
        elif "full screen" in query :
            keyboard.press("f")
        elif "exit full screen" in query :
            keyboard.press("f")
        elif "film mode" in query :
            keyboard.press("t")
        elif "pause" in query:
            keyboard.press("k")
        elif 'gmail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shivangrustagi004@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")
        elif 'exit' in query:
            speak("Goodbye!")
            exit
if __name__ == "__main__":
    main()