from midiToCsv import midiToCsv
from csvToCsv import csvToCsv
from serialWriter import serialWriter
from csvToBin import csvToBin
from serialWriterBin import serialWriterBin
import os.path

def main(input):
    name, _ = input.split(".")
    if(not os.path.isfile(name+".szk")):
        midiToCsv(input, "tmp.csv")
        csvToCsv("tmp.csv", name+".csv")
        csvToBin(name+".csv", name+".szk")
    serialWriterBin(name+".szk")

if __name__ == "__main__":
    input = "furelise.mid"
    main(input)