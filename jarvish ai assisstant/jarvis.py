import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai  # Import Gemini AI SDK

# Initialize API Key
genai.configure(api_key="AIzaSyAwgW3SYl4MubXSCUp_aZMvVchR4yaMzv0")

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "96f1daee5c2b405e8d4e0e7860d45af7"


def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()


def ask_gemini(prompt):
    """Generate a response from Gemini AI"""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error using Gemini: {e}"


def processCommand(command):
    """Process user commands"""
    print(f"Command received: {command}")
    command = command.lower()

    if "open google" in command:
        speak("OK! opening Google")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command:
        speak("OK! opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command:
        speak("OK! opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open youtube" in command:
        speak("OK! opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith("play"):
        song = " ".join(command.split(" ")[1:])
        if song in musiclibrary.music:
            link = musiclibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I don't have {song} in the music library.")

    elif "news" in command:
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
            )
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
                speak("Sorry, I couldn't fetch the news at this moment.")
        except Exception as e:
            print(f"Error fetching news: {e}")
            speak("There was an error while fetching the news.")

    elif "jarvis" in command:
        prompt = command.replace("jarvis", "").strip()  # Remove 'Jarvis' from the query
        gemini_response = ask_gemini(prompt)
        speak(gemini_response)  # Speak Gemini AI's response
        print(f"Gemini AI: {gemini_response}")

    else:
        speak("I didn't understand that command.")


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis activated")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
