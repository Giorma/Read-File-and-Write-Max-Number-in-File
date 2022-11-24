def max_num_in_file(filename):
    with open(filename, "r") as f:
        data = [int(x) for x in f.readlines()]
    return max(data)


# here we enter number in file
with open("./file/txt", "w") as f:
    for i in range(10):
        num = input("Enter Number: ")
        f.writelines(num + "\n")

answer = max_num_in_file('./file/txt')
with open("./file/txt", "w") as f:
    f.write(str(answer))

print(f"Largest number in file: {answer}")