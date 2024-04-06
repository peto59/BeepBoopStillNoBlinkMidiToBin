with open("test.csv", "r") as csv:
    with open("out.szk", "wb") as binary_file:
        for line in csv:
            data = line[:-1].split(";")
            value_bytes = int(data[0]).to_bytes(2, byteorder='big', signed=False)
            binary_file.write(value_bytes)
            value_bytes = int(data[1]).to_bytes(8, byteorder='big', signed=False)
            binary_file.write(value_bytes)
            value_bytes = int(data[2]).to_bytes(8, byteorder='big', signed=False)
            binary_file.write(value_bytes)