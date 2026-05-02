import csv


def tempo_to_bpm(tempo_local):
    return 60000000 / tempo_local


def ticks_to_milliseconds(ticks_local, bpm_local, ppq_local):
    return (60000 / bpm_local) * (ticks_local / ppq_local)


def select_single_note(active_notes):
    if not active_notes:
        return None
    return max(active_notes)


def csvToCsv(input, output):
    ppq = 480
    bpm = 120
    events = []

    with open(input, 'r') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            if not row:
                continue

            first_cell = row[0].strip()
            if first_cell.startswith('#') or first_cell.startswith(';'):
                continue

            record_type = row[2].strip()
            tick = int(row[1])

            if record_type == 'Header':
                ppq = int(row[5])
                continue

            if record_type == 'Tempo':
                events.append((tick, 0, 'tempo', int(row[3])))
                continue

            if record_type == 'Note_off_c':
                events.append((tick, 1, 'note_off', int(row[4])))
                continue

            if record_type == 'Note_on_c':
                note = int(row[4])
                velocity = int(row[5])
                if velocity == 0:
                    events.append((tick, 1, 'note_off', note))
                else:
                    events.append((tick, 2, 'note_on', note))

    events.sort(key=lambda event: (event[0], event[1]))

    active_notes = {}
    current_tick = 0
    current_bpm = bpm
    pending_note = None
    pending_duration_ms = 0.0

    def flush_pending(csv_output):
        nonlocal pending_note, pending_duration_ms
        if pending_note is None:
            return

        duration_ms = round(pending_duration_ms)
        if(duration_ms == 0):
            return
        assert 0 <= duration_ms <= 65535
        csv_output.write(f"{pending_note},{duration_ms}\n")
        pending_note = None
        pending_duration_ms = 0.0

    with open(output, "w") as csvOutput:
        for tick, _, event_type, value in events:
            delta_ticks = tick - current_tick
            if delta_ticks > 0:
                delta_ms = ticks_to_milliseconds(delta_ticks, current_bpm, ppq)
                if pending_note is not None:
                    pending_duration_ms += delta_ms
                current_tick = tick

            if event_type == 'tempo':
                current_bpm = tempo_to_bpm(value)
                continue

            if event_type == 'note_on':
                active_notes[value] = active_notes.get(value, 0) + 1
            else:
                if value in active_notes:
                    active_notes[value] -= 1
                    if active_notes[value] <= 0:
                        del active_notes[value]

            next_note = select_single_note(active_notes)

            if next_note != pending_note:
                flush_pending(csvOutput)
                pending_note = next_note

        flush_pending(csvOutput)


if __name__ == "__main__":
    a = 'in.csv'
    b = "furelise.csv"
    csvToCsv(a, b)

