# Program to turn a list into a string with values
# separated by commas

def makeString(list):
    myString = ""
    for item in list:
        # If value isn't last, add it to string with a comma
        if list.index(item) != len(list) - 1:
            myString += item + ", "
        # If value is last, add "and value" at the end
        else:
            lastWord = "and " + item
            myString += lastWord
    return myString

# Tests
theList = ["apples", "bananas", "tofu", "cats"]
print(makeString(theList))
