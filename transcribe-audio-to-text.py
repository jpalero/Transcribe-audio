import os
import speech_recognition as sr

def transcribe_audio(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Transcribe the audio
        text = recognizer.recognize_google(audio_data)
        print("Transcription:")
        print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

    # Save the transcription to a text file
    with open("transcription.txt", "w") as text_file:
        text_file.write(text)

    print("Transcription saved as transcription.txt")

if __name__ == "__main__":
    # Define the path to the audio file you want to transcribe
    # Replace with the actual path to your audio file
    AUDIO_FILE_PATH = "C:\\Users\\jsonp\\OneDrive\\Desktop\\Output-record\\Sample.wav"

    # Transcribe the audio and save the transcription to a text file
    transcribe_audio(AUDIO_FILE_PATH)
