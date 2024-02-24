# Import necessary libraries 
import moviepy.editor as mp # Used for extracting audio from video files
import speech_recognition as sr # For converting speech to text
from googletrans import Translator # For translating text from one language to another
import os # For file and directory operations

# Path to your MP4 video file
video_file_path = r'C:\Users\owner\Documents\my_project\Youtube-Edit-Supporter\audio input\video.mp4'

# Load the video file
video = mp.VideoFileClip(video_file_path)

# Extract audio from the video
audio = video.audio

# Save the audio to a file with minor background noises reduced
audio_file_path = r'C:\Users\owner\Documents\my_project\Youtube-Edit-Supporter\audio output\noise_reduced_audio.wav'
audio.write_audiofile(audio_file_path)

# Close the video file
video.close()

# Display a processing message
print("\033[92mProcessing... Please wait.\033[0m")

# Initialize the speech recognizer and load the audio file
# This section covers converting the audio to text using Google's Web Speech API and translating the text from Hebrew (or Arabic) to English.
r = sr.Recognizer()

# Load the audio file
with sr.AudioFile(audio_file_path) as source:
    # Listen to the audio file
    audio_data = r.record(source)

    # Try to recognize speech using Google Web Speech API
    try:
        # Assuming the video language is Hebrew; change 'he-IL' to 'ar-SA' for Arabic
        text = r.recognize_google(audio_data, language='he-IL')
        
        # Translate the transcribed text into English
        translator = Translator()
        translated = translator.translate(text, src='he', dest='en')
        
        # Prepare the text to be saved, including both the original and translated texts
        output_text = f"Original Text (Hebrew):\n{text}\n\nTranslated Text (English):\n{translated.text}"
        print(output_text)
        
        # Save the output text to a file in the specified "text output" folder
        output_file_path = r'C:\Users\owner\Documents\my_project\Youtube-Edit-Supporter\text output\text_output.txt'
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(output_text)

    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")
