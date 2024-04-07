import serial
import time
def serialWriter(input):
    num = 0
    s = serial.Serial('COM3', 115200)
    with open(input, "r") as csv:
            for line in csv:
                num += 1
                print(num, line)
                data = line[:-1].split(",")
                value_bytes = int(data[0]).to_bytes(2, byteorder='big', signed=False)
                s.write(value_bytes)
                value_bytes = int(data[1]).to_bytes(8, byteorder='big', signed=False)
                s.write(value_bytes)
                value_bytes = int(data[2]).to_bytes(8, byteorder='big', signed=False)
                s.write(value_bytes)
                time.sleep(((int(data[2])-int(data[1]))/1000))

if __name__ == "__main__":
     serialWriter("mid.csv")
# res = s.write("abcdefghijkl".encode())
# print(res)
# res = s.read(12)
# print(res)