# =====================================
# simple string in python
# created by Amit Barman
# https://www.github.com/amit-barman
# =====================================

# importing os
import os

# take input string from user
val = input("Enter your value: ")
print("\n")

def isbinod(filename) :
    with open(filename, "r") as f :
        fileContent = f.read()

    # if val in another form like strIng
    if val in fileContent.lower() :
        return True
    else :
        return False

if __name__ == "__main__" :
    # listing the containt of this folder
    dir_contents = os.listdir()

nval = 0
# for each text file run isbinod for them
for item in dir_contents :
    if item.endswith("txt") :
        print(f"Detecting {val} in {item}")
        flag = isbinod(item)
        if (flag) :
            print(f"++++ {val} find in {item} ++++")
            nval += 1
        else :
            print(f"---- {val} not found in {item} ----")
            print("\n")

print("\n")
print("String detecter summary")
print("\n")
print(f"{nval} file found with {val} present into them")