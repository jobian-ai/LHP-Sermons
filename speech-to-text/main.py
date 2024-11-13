import whisper
import numpy as np

model = whisper.load_model("medium.en")

# result = model.transcribe(r"Z:\_Audio\2024.06.30-DOVE.mp3")
result = model.transcribe(r"C:\Users\Chuck\Music\The Greatest Takedown of the Pro-Choice Position You’ve Ever Heard [-txhf3UOiyA].m4a")


with open("transcription-med-en.txt", "w") as f:
    f.write(result["text"])
c