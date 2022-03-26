import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()
voice_input = engine.say("Start talking...")
engine.runAndWait()
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 0.3)
        print("Speak Now")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("Speaker: ", text)

            if text == "quit":
                break
        except:
            print("please say again")
