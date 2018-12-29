import textract
import encodings
import os

def convert_to_text(file_path):
    """
        Error codes:
            1- "01" > file corraped or with no format
            2- "10" > file has format rather than pdf, txt or equb
            3- "11" > Error while extracting text from the 
            4- "00" > Error while opening the file
    """
    try:
        file_name = file_path.split("/")[2]
        file_format = file_name.split(".")[1]
    
    except:
        return "01"

    supported_formats = ["pdf", "txt", "equb", "PDF", "TXT", "EQUB"]

    if file_format not in supported_formats:
        return "10"
    
    try:
        #try to open the file
        input_file = open(os.getcwd() + file_path, "r")
        try:
            text = textract.process(os.getcwd() + file_path)
            text = text.decode("utf-8", 'ignore')
            return text
        
        except:
            return "11"
    except:
        return "00"
