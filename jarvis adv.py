import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import datetime
import wikipedia
import os
import smtplib
import pygame
 
Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
print(voices)
Assistant.setProperty("voices",voices[0].id)
Assistant.setProperty("rate",150)
def speak(audio):
    print("   ")
    Assistant.say(audio)
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("recognizing.....")
            query = command.recognize_google(audio, language="en - in")
            print(f"you said : {query}")

        except Exception as error:
            return "none"
        
        return query.lower()

# query = takecommand()

# if "hello" in query:
#     speak("hello sir")

# else:
#     speak("no command found")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def taskexe(): 

    while True:
        query = takecommand()

        if "hello" in query:
            speak("hello sir, i am jarvis ")
            speak("i am your ai assistant")
            speak("how can i help you ")
        elif "how are you " in query:
            speak(" i am fine sir thank you for asking")
        elif "you need break" in query:
            speak("arlight you can call me anytime")
            break

        elif " kya haal hai" in query:
            speak("sab jhakaas hai")
        elif "bye"in query:
            speak("have a good day ahead")
            break

        elif "main aacha hoon tum batao" in query:
            speak("main bhi")
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
            name = takecommand()
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

        elif 'gmail to shivang' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "shivangrustagi004@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email")

        elif 'exit' in query:
            speak("Goodbye!")
            exit()
            

        
            