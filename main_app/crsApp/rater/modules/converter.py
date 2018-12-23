import textract
import encodings
import os

def convert_to_text(file_path):
    try:
        file_name = file_path.split("/")[2]
        file_format = file_name.split(".")[1]
    except:
        return ("Please Try another file please!")

    supported_formats = ["pdf", "txt", "equb", "PDF", "TXT", "EQUB"]

    if file_format not in supported_formats:
        return ("Try different file formats please!")
    try:
        text = textract.process(os.getcwd() + file_path)
        text = text.decode("utf-8")
        return text
    except:
        return ("Please Try another file please!")
