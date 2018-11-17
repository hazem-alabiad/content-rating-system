import os

#Parse the translate file inside the translates_path directory to the output_path directory
def parse_translates(translates_path, output_path):
    file_number = 1
    
    for directory_name in os.listdir(translates_path):
        translate_file_name = os.listdir(os.path.join(translates_path, directory_name))[0]
        film_rating = directory_name.split("_")[0]
        print(film_rating)

        read_file = open(os.path.join(translates_path, directory_name, translate_file_name), encoding = "utf-8", errors="ignore")
        write_file = open(os.path.join(output_path, film_rating + "_" + str(file_number)), "w")
        file_number +=1

        write_buffer = ""
        lines_count = 0
        lines = []

        for line in read_file:
            line=str(line)
            if line[0] == '\n':
                for i, already_read_lines in enumerate(lines):
                    if i != 0 and i !=1:
                        already_read_lines = already_read_lines.split('\n')[0]
                        write_buffer = write_buffer + already_read_lines
                        write_buffer = write_buffer + " "
                
                lines = []
            else:
                lines.append(line)

        write_file.write(write_buffer)

        read_file.close()
        write_file.close()

