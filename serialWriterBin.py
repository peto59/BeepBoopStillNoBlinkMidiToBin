import serial
import time
from pathlib import Path

def serialWriterBin():
    num = 0
    s = serial.Serial('/dev/ttyACM0', 115200)
    requested = False
    requested_filename = ""
    requested_file_size = 0
    while True:
        if( not requested):
            request = s.read_until(expected=b'\x00');
            print("raw request: ", request.hex())
            if(request == b"\x00"):
                continue
            
            if(request == b'info\x00'):
                c_strings = []
                for f in Path(".").glob("*.szk"):
                    name_bytes = f.stem.encode("ascii")
                    c_string = bytearray(name_bytes[:15] + b"\x00")
                    c_strings.append(c_string)
                print(c_strings)

                value_bytes = int(len(c_strings)).to_bytes(1, byteorder='little', signed=False)
                s.write(value_bytes)

                for string in c_strings:
                    s.write(string)

                continue

            try:
                requested_filename = (b"./" + request.rstrip(b"\x00") + b".szk").decode("ascii")
                print("requested song: ", requested_filename)
                requested_file_size = Path(requested_filename).stat().st_size
                assert requested_file_size % 3 == 0
                requested_file_size //= 3
                print("song size: ", requested_file_size, "notes")
                value_bytes = int(requested_file_size).to_bytes(8, byteorder='little', signed=False)
                s.write(value_bytes)
                requested = True

                continue
            except:
                continue

        with open(requested_filename, "rb") as file:
            requested = False
            while requested_file_size > 0:
                size = int.from_bytes(s.read(2), byteorder='little', signed=False)
                if(size == 0):
                    print("stopped")
                    break
                print("requested size: ", size)
                requested_file_size -= size
                data = file.read(size * 3)
                if not data:
                    assert(False)
                s.write(data)
