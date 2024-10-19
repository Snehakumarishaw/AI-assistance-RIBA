import pyttsx3
import distutils
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening....")
       recognizer.adjust_for_ambient_noise(source)
       audio = recognizer.listen(source)
       try:
          print("recognizing....")
          data = recognizer.recognize_google(audio)
          print(data)
          return data
       except sr.UnknownValueError:
           print("Not Understand")
           
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()
#speechtx("Good morning!Sneha i hope you are doing well ! how can i help you ")

if __name__ == '__main__':

    if "hey Riba" in sptext().lower():
        while True :
                data1=sptext().lower()

                if "your name" in data1:
                    name = " my name is Riba "
                    speechtx(name)
                elif "old are you" in data1:
                    age = "i am twenty years old"
                    speechtx(age)

                elif 'time' in data1:#display the date and time
                    time = datetime.datetime.now().strftime("%I%M%p")
                    speechtx(time)
                    
                elif'youtube' in data1: #open webbrowser
                    webbrowser.open("https://www.youtube.com/")

                elif 'joke' in data1:#display random jokes form pyjokes library
                    joke_1 = pyjokes.get_joke(language="en",category="neutral")
                    print(joke_1)
                    speechtx(joke_1)
                    
                elif'show img' in data1: #display the image from the system
                    addr = "C:\Users\sneha\Pictures\Camera Roll\Gemini_Generated_Image_wxyq22wxyq22wxyq.jpeg"
                    listimg = os.listdir(addr)
                    print(listimg)
                    os.startfile(os.path.join(addr,listimg[1]))

                elif "exit" in data1:
                    speechtx("thank you")
                    break
                
                time.sleep(5)
                

            
                #print(time)
        else:
            print("Thanks!")
        
    
