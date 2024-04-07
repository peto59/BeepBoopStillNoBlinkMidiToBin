import serial
import time
def serialWriterBin(input):
    num = 0
    s = serial.Serial('COM3', 115200)
    with open(input, "rb") as file:
            while True:
                data = file.read(18)
                if not data:
                    break
                s.write(data)
                start = int.from_bytes(data[2:10], byteorder='big')
                end = int.from_bytes(data[10:], byteorder='big')
                time.sleep(((end-start)/1000))

if __name__ == "__main__":
    serialWriterBin("furelise.szk")
# res = s.write("abcdefghijkl".encode())
# print(res)
# res = s.read(12)
# print(res)