Friday - Voice Assistant 🗣️

Friday is a Python-based voice assistant that listens for the wake word **"Friday"** and performs smart tasks such as opening websites, playing songs, and fetching news headlines. 📰🎶

  ✨ Features
- 🎤 Speech Recognition using `speech_recognition`
- 🔊 Text-to-Speech powered by `pyttsx3`
- 🎵 Play Music from a custom library (`musicLib.py`)
- 🗞️ Get Latest News using the News API
- 🌐 Only open Websites like Google and YouTube via voice commands

 ⚙️ Requirements
Install dependencies before running the assistant:
```bash
pip install speechrecognition pyttsx3 requests
```

 🚀 How to Run
1. Make sure your microphone is connected and working.
2. Run the assistant using:
   ```bash
   python main.py
   ```
3. Say "Friday" to activate, then give a command such as:
   - `open google`
   - `open youtube`
   - `play dragon`
   - `news`

📁 Project Structure
```
main.py        # Main program controlling Friday
musicLib.py    # Song links used by Friday to play music
```

 🧠 Example Commands
| Command | Action |
|----------|---------|
| "Friday, open Google" | Opens Google in your browser |
| "Friday, play bleach" | Plays the song from YouTube |
| "Friday, news" | Reads top 5 headlines |

---
> “Friday is always listening for your next command!”
