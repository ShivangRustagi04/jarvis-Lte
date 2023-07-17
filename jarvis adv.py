import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
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
        
            