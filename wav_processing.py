import sys

def wav_process(input_filename,output_filename):
    with open(input_filename, "r") as input_file, open(output_filename, "w") as output_file:
        previous_line = None
        for line in input_file:
            line = line.rstrip()
            if previous_line is not None and (line.startswith(" ") or line.isalpha()):
                previous_line += " " + line
            else:
                if previous_line is not None:
                    output_file.write(previous_line + "\n")
                previous_line = line

if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    wav_process(input_filename, output_filename)
