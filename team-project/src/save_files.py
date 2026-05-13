def save_transcript(transcript, filename="raw_transcript.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(transcript + "\n")  