from midiToCsv import midiToCsv
from csvToCsv import csvToCsv
from serialWriter import serialWriter
from csvToBin import csvToBin
from serialWriterBin import serialWriterBin
import os.path

def main(input):
    name, _ = input.split(".")
    if(not os.path.isfile(name+".szk")):
        if(not os.path.isfile(name+".csv")):
            midiToCsv(input, "tmp.csv")
            csvToCsv("tmp.csv", name+".csv")
        csvToBin(name+".csv", name+".szk")

if __name__ == "__main__":
    for i in ["furelise.mid", "fireflies.mid", "gravityfalls.mid", "wakemeup.mid", "cruelangel.mid", "unravel.mid", "levels.mid", "dearlybeloved.mid", "light.mid", "hallking.mid", "patamat.mid"]:
        
        print(i)
        main(i)
    while True:
        try:
            serialWriterBin()
        except KeyboardInterrupt:
            break
        except:
            continue

