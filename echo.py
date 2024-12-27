#pip install SpeechRecognition
import speech_recognition as sr
#pip install pyttsx3
import pyttsx3
#pip install pyaudio

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Ready")
engine.runAndWait()
numbers = []

while True:
    try:
    
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            recorded_audio = recognizer.listen(source, timeout=10)

        text = recognizer.recognize_google(recorded_audio, language="en-US")
        text = text.strip()       

        if text:
        
            try:
                result = int(''.join(filter(str.isdigit, text)))
            except Exception as error:
                result = None
        
            if 'exit' in text.lower():
                engine.say("Goodbye")
                engine.runAndWait()
                break
                
            if 'last' in text.lower():
                engine.say(numbers[-1])
                print(numbers[-1])
                
            if 'first' in text.lower():
                engine.say(numbers[0])
                print(numbers[0])
                
            if 'all' in text.lower():
                engine.say(str(numbers))
                print(numbers)
                
            if 'clear' in text.lower():
                print(numbers)
                numbers = []
                print(numbers)
    
            if result:
               numbers.append(result)
               print(numbers)
               engine.say(result)

        engine.runAndWait()

    except Exception as error:
        print(str(error))
