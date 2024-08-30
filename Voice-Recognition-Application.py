import speech_recognition as sr
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

def execute_command(command):
    """Executes commands based on recognized keywords."""
    if "hello" in command:
        print("Hello! How can I assist you today?")
    elif "open notepad" in command:
        os.system("notepad")
    elif "play music" in command:
        os.system("start wmplayer")  # For Windows Media Player on Windows
    elif "exit" in command:
        print("Exiting...")
        return False
    else:
        print("Command not recognized.")
    return True

def main():
    """Main function to listen for audio and process commands."""
    with sr.Microphone() as source:
        print("Listening for commands...")
        while True:
            try:
                audio = recognizer.listen(source)
                print("Processing...")
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")
                if not execute_command(command):
                    break
            except sr.UnknownValueError:
                print("Sorry, I didn't catch that.")
            except sr.RequestError:
                print("Sorry, there's an issue with the speech recognition service.")

if __name__ == "__main__":
    main()
