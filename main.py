import os 
import win32com.client
import speech_recognition as sr

speaker=win32com.client.Dispatch("SAPI.SpVoice")

def Say(Text):
    # print("enter the word you want to speak ")
    # print("listening..")
    s=Text
    speaker.speak(s)
    return print(Text)
    
    
    
def takecommand():  
    print("Listening ...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
        # print("Listening ...")
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"
        
        
Say("Hii  what i can help you with") 
takecommand()
    
# Say("gooooooooooooooooooooooooooooooooooooooooodd")