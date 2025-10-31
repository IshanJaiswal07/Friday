import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import requests
import logging

# --- Setup ---
# Suppress unnecessary warnings from the speech_recognition library
logging.getLogger("speech_recognition").setLevel(logging.ERROR)

recognizer = sr.Recognizer()
engine = pyttsx3.init()

# IMPORTANT: Add your country code (e.g., 'us' for USA, 'in' for India)
# The API will not work without a country specified.
NEWS_API_KEY = "ae267e777c514f819619390a9b22d514"
NEWS_COUNTRY_CODE = "us" 

def speak(text):
    """Converts text to speech."""
    print(f"Friday: {text}")
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speak(): {e}")

def processCommand(c):
    """Processes the given voice command."""
    command = c.lower()
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith("play"):
        # Assumes format "play [songname]"
        song_parts = command.split(" ")
        if len(song_parts) > 1:
            song = song_parts[1]
            if song in musicLib.music:
                link = musicLib.music[song]
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, I don't have the song {song} in my library.")
        else:
            speak("Please specify which song to play.")

    elif "news" in command:
        speak("Fetching the latest news headlines.")
        url = f"https://newsapi.org/v2/top-headlines?country={NEWS_COUNTRY_CODE}&apiKey={NEWS_API_KEY}"
        r = requests.get(url)

        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            if not articles:
                speak("Sorry, I couldn't retrieve any news articles.")
                return

            speak("Here are the top 5 headlines:")
            # Read only the top 5 articles to save time
            for article in articles[:5]:
                speak(article["title"])
        else:
            speak(f"Sorry, I failed to fetch news. The service returned a status code of {r.status_code}.")

def listen_for_wake_word():
    """Listens for the wake word 'Friday'."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening for wake word...")
            audio = r.listen(source, timeout=5, phrase_time_limit=3)
        
        word = r.recognize_google(audio)
        if "friday" in word.lower():
            return True
    except sr.UnknownValueError:
        # This happens when speech is unintelligible
        pass
    except sr.WaitTimeoutError:
        # This happens if no speech is detected within the timeout
        pass
    except Exception as e:
        print(f"Error during wake word detection: {e}")
    
    return False

def listen_for_command():
    """Listens for a command after the wake word is detected."""
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 0.8
            r.adjust_for_ambient_noise(source, duration=1)
            print("Friday Active... How can I help?")
            audio = r.listen(source)
        
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please try again.")
    except Exception as e:
        speak("An error occurred while listening for your command.")
        print(f"Command listening error: {e}")
    
    return ""


if __name__ == "__main__":
    speak("Initializing Friday...")
    while True:
        if listen_for_wake_word():
            speak("Hello sir")
            command = listen_for_command()
            if command:
                processCommand(command)