import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "new api key "
genai.configure(api_key="gemini api key")
r=None

def speak(text):
    engine.say(text)
    engine.runAndWait()


def aiProcess(command):
    try:
        # Initialize the Gemini model
        model = genai.GenerativeModel("gemini-1.5-pro")

        # Generate AI response
        response = model.generate_content([command])

        # Check if the response is valid
        if response and hasattr(response, "text"):
            return response.text
        else:
            return "Sorry, I couldn't process that request."

    except Exception as e:
        return f"Error: {str(e)}"


def processCommand(c):
    print(f"command received: {command}")

    if "open google" in command.lower():
        speak("OK! opening google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command.lower():
        speak("OK! opening facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command.lower():
        speak("OK! opening linkedin")
        webbrowser.open("https://www.linkedin.com")

    elif "open youtube" in command.lower():
        speak("OK! opening youtube")
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        # c.lower().split(" ")[1]
        song = song = " ".join(c.lower().split(" ")[1:])

        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if not articles:
                    speak("Sorry, no news articles found.")
                else:
                    speak("Here are the top 5 news headlines.")
                    for i, article in enumerate(articles[:5]):
                        speak(f"News {i+1}: {article['title']}")
            else:
                speak("Sorry! I couldn't fetch the news at this moment.")
        except Exception as e:
            print(f"Error fetching news: {e}")
            speak("There was an error while fetching the news.")   
    else:
        response = aiProcess(command)
        speak(response)
  

if __name__=="__main__":  
    speak("initialling jarvis...") 
    while True:
        
        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening...")
                
                audio=recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word= recognizer.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes how can i help you !")
                with sr.Microphone() as source:
                    print("jarvis activated")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio=recognizer.listen(source)
                    command=recognizer.recognize_google(audio)
                    
                    processCommand(command)
        except Exception as e:
            print(f"Error:{e}")
