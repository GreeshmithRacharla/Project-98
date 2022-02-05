
file1 = "sample1.txt"
data_b = ""


def swapFileData():
    input1 = input("Enter the file name: ")

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file1, 'w') as a:
        a.write(data_b)


swapFileData()
    