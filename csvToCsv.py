import csv
def tempo_to_bpm(tempo_local):
    return 60000000 / tempo_local
def ticks_to_milliseconds(ticks_local, bpm_local, ppq_local):
    return (60000 / bpm_local) * (ticks_local / ppq_local)
def midi_note_to_frequency(midi_note):
    return 440 * 2**((midi_note - 69) / 12)
def csvToCsv(input, output):
    last_start = -1
    ppq = 480
    bpm = 120
    with open(input, 'r') as csvfile:
        reader = csv.reader(csvfile)
        with open(output, "w") as csvOutput:
            for row in reader:
                # print(row)

                if row[2] == ' Header':
                    ppq = int(row[5][1:])
                if row[2] == ' Tempo':
                    bpm = tempo_to_bpm(int(row[3][1:]))
                if row[2] == ' Note_on_c' or row[2] == ' Note_off_c':

                    
                    if row[2] == ' Note_off_c':
                        note_frequency = 0
                    else:
                        note_frequency = midi_note_to_frequency(int(row[4][1:])) 

                    start_position_ms = ticks_to_milliseconds(int(row[1][1:]), bpm, ppq) 
                    if(round(last_start) == round(start_position_ms)):
                        # print(note_frequency, start_position_ms)
                        continue
                    if(last_start != -1):
                        csvOutput.write(f"{round(start_position_ms)}\n")
                    last_start = start_position_ms
                    
                    csvOutput.write(f"{round(note_frequency)},{round(start_position_ms)},")
            csvOutput.write(f"{round(start_position_ms)}\n")

if __name__ == "__main__":
    a = 'in.csv'
    b = "furelise.csv"
    csvToCsv(a,b)