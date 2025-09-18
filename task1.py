try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(line.strip())   # strip() removes extra spaces/newlines
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")