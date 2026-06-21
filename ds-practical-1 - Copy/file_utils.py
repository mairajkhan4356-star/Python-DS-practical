def write_file():
    f = open("data.txt", "w")
    f.write("Hello bro")
    f.close()

def read_file():
    f = open("data.txt", "r")
    print(f.read())
    f.close()
