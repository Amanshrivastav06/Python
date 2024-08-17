
import speech_recognition as sr
import webbrowser
import pyttsx3  # it is for text to speech conversion
import musicLibrary
import pywhatkit as kit
recognizer = sr.Recognizer() # Creates a new Recognizer instance, which represents a collection of speech recognition functionality
engine = pyttsx3.init() # this is for intialising ttsx

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c): 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "play" in c.lower():  # To play a song on YouTube        ** ye pywhatkit use kiya so i don't need to use musiclibrary
        song = c.lower().replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        kit.playonyt(song)

    elif "search" in c.lower():  # To search something on Google
        query = c.lower().replace("search", "").strip()
        speak(f"Searching for {query} on Google")
        kit.search(query)
    
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))
