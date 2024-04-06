import serial
import time
num = 0
s = serial.Serial('COM3', 9600)
with open("Mario_Brothers_theme.csv", "r") as csv:
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
            time.sleep((int(data[2])-int(data[1]))/1000)
# res = s.write("abcdefghijkl".encode())
# print(res)
# res = s.read(12)
# print(res)