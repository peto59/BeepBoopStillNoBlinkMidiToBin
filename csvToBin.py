def csvToBin(input, output):
    with open(input, "r") as csv:
        with open(output, "wb") as binary_file:
            for line in csv:
                try:
                    data = line[:-1].split(",")
                except:
                    data = line[:-1].split(";")
                value_bytes = int(data[0]).to_bytes(2, byteorder='big', signed=False)
                binary_file.write(value_bytes)
                value_bytes = int(data[1]).to_bytes(8, byteorder='big', signed=False)
                binary_file.write(value_bytes)
                value_bytes = int(data[2]).to_bytes(8, byteorder='big', signed=False)
                binary_file.write(value_bytes)


if __name__ == "__main__":
    a = "mariobros.csv"
    b = "mariobros.szk"
    csvToBin(a,b)