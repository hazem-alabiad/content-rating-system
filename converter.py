import textract
import encodings
import os

def covert_to_text(file_path):
    try:
        file_format = os.path.relpath(file_path).split(".")[1]
    except:
        return ("Please Try another file please!")

    supported_formats = ["pdf", "txt", "equb"]

    if file_format not in supported_formats:
        return ("Try different file formats please!")

    try:
        text = textract.process(file_path)
        text = text.decode("utf-8")
        return text
    except:
        return ("Please Try another file please!")
