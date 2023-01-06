import pyttsx3
import openai
import os
import speech_recognition as sr
engine = pyttsx3.init()
voices = engine.getProperty('voices')



engine.setProperty("voice", voices[0].id)
openai.api_key = "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"
z=0
print("inserisci 1 per usare i comandi vocali o 0 premi per continuare ")
h = int(input())
while z == 0:

 if h==1:
    recognizer_instance = sr.Recognizer()
    with sr.Microphone() as source:
     print("Sono in ascolto... parla pure!")
     audio = recognizer_instance.listen(source)
     a = recognizer_instance.recognize_google(audio, language="it-IT")
     print(":", a)
 elif h==0:
     print("inserisci la richiesta")
     a=input(":")
 try:
        a = "Write an extremely short, detailed answer to \"" + a + "\".  HTML formatting."

        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=a,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        r = response.choices[0].text
        print(r)
        if h==1:
         engine.say(r)
         engine.runAndWait()

        input("press to continue...")
        os.system('cls')

 except Exception as e:
    print("errore")
    input("press to continue...")
    os.system('cls')

