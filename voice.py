import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            recognized_text = recognizer.recognize_google(audio)
            print("You said:", recognized_text)
            
            if "hello" in recognized_text.lower():
                speak("Hello! How can I assist you?")
            else:
                speak("I'm sorry, I didn't understand that.")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
