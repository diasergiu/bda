from src.gemini_correct import ask_gemini_to_correct
from src.vosk_microphone import record_and_transcribe
from src.save_files import save_transcript
from datetime import datetime

if __name__ == "__main__":
   
    number_of_team_members = int(input("Enter the number of team members speaking: "))
    for _ in range(number_of_team_members):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        name = input("Enter the name of the speaker: ")
        raw_text = record_and_transcribe()
        print("Original transcript:", raw_text)
        output = ask_gemini_to_correct(raw_text)
        print("Corrected transcript:", output)