import textract
import encodings

def covert_to_text(file_path):
    
    text = textract.process(file_path)

    text = text.decode("utf-8")

    return text