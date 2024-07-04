import whisper
import numpy as np

model = whisper.load_model("medium.en")

result = model.transcribe(r"Z:\_Audio\2024.06.30-DOVE.mp3")

with open("transcription-med-en.txt", "w") as f:
    f.write(result["text"])
