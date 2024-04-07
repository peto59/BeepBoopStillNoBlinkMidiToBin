import subprocess

def midiToCsv(input, output):
    # Define the command and arguments
    command = ["./midicsv-1.1/Midicsv.exe", input]

    # Redirect the output to a file
    with open(output, "w") as output_file:
        # Execute the command
        subprocess.run(command, stdout=output_file)

if __name__ == "__main__":
    midiToCsv("furelise.mid", "in.csv")