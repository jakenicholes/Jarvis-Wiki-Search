#Name:   jarvis.py
#Author: Jake Nicholes
#Date:   2/18/2026

import speech_recognition as sr
import pyttsx3
from wikipedia_oop import WikipediaApp
from sys import exit

class JarvisAI:
    def __init__(self):
        #Create SR object and TTS engine, set TTS properties
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.RATE = 150
        self.VOLUME = 1.0
        self.VOICE = 0
        self.engine.setProperty("rate", self.RATE)
        self.engine.setProperty("volume", self.VOLUME)
        self.engine.setProperty("voice", self.engine.getProperty("voices")[self.VOICE].id)

    #Define speaking method
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    #have an initial greeting method
    def initial_greeting(self):
        print("Hello, sir. How can I help you?")
        self.speak("Hello sir. How can I help you?")

    #Create a method to respond to user input, and exit if user says "Goodbye Jarvis"
    def respond_to_input(self, recognized_words):
        if "goodbye".lower() in recognized_words.lower():
            self.speak("Goodbye, sir!")
            exit()
        else:
            wiki_response = self.get_wiki_response(recognized_words)
            print(f"Wikipedia says: {wiki_response}")
            self.speak(wiki_response)

    #Create a method to get the wiki response
    def get_wiki_response(self, search_term):
        wiki_response = WikipediaApp().get_wikipedia(search_term)
        return wiki_response
    
    #Create a method to loop through conversation, listen for user input, and respond to user input
    def conversation_loop(self):
        #With local microphone source
        while True:
            #Flush microphone source before listening again
            self.engine.stop()

            with sr.Microphone() as source:
                #Listen for user input
                print("Listening. . .")
                audio = self.r.listen(source)

            try:
                print("Recognizing. . .")

                recognized_words = self.r.recognize_google(
                    audio,
                    language = "en-US",
                    show_all = True
                )

                recognized_words = recognized_words.get("alternative")[0].get("transcript")
                print(f"You said: {recognized_words}")

                self.respond_to_input(recognized_words)

            except sr.UnknownValueError:
                print("I could not understand what you said.")

            except sr.RequestError as e:
                print(f"Error: {e}")

def main():
    jarvis = JarvisAI()
    jarvis.initial_greeting()
    jarvis.conversation_loop()

if __name__ == "__main__":
    main()