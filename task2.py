u1 = input("Enter text to write to te file: ")
with open("output.txt", "w") as file:
    file.write(u1 + "\n")
    print("Data successful written to output.txt")

e1 = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(e1 + "\n")
    print("Data successful appended")


print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())

