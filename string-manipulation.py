
def camel2Pascal(camelText):

    pascalText = camelText[0].upper() + camelText[1:]
    return pascalText

def pascal2Camel(pascalText):

    camelText = pascalText[0].lower() + pascalText[1:]
    return camelText



def test_camel2Pascal(test_number, inputText, expectedOutput):
    print(f"{test_number}. Input = {inputText}")
    print(f"{test_number}. Expected Output = {expectedOutput}")
    actualOutput = camel2Pascal(inputText)
    print(f"{test_number}. Actual Output = {actualOutput}")

    if actualOutput == expectedOutput:
        print("Output correct")
        return True
    else:
        print("OUTPUT INCORRECT")
        return False

def test_pascal2Camel(test_number, inputText, expectedOutput):
    print(f"{test_number}. Input = {inputText}")
    print(f"{test_number}. Expected Output = {expectedOutput}")
    actualOutput = pascal2Camel(inputText)
    print(f"{test_number}. Actual Output = {actualOutput}")

    if actualOutput == expectedOutput:
        print("Output correct")
        return True
    else:
        print("OUTPUT INCORRECT")
        return False

print("Testing: camel2Pascal")
print("=====================")
test_camel2Pascal(1, "oneTwoThree", "OneTwoThree")
test_camel2Pascal(2, "1TwoThree", "1TwoThree")
test_camel2Pascal(3, "_TwoThree", "_TwoThree")
test_camel2Pascal(4, "'TwoThree", "'TwoThree")
test_camel2Pascal(5, "\nTwoThree", "\nTwoThree")
test_camel2Pascal(6, "OneTwoThree", "OneTwoThree")

print("\n\nTesting: pascal2Camel")
print("=====================")
test_pascal2Camel(1, "OneTwoThree", "oneTwoThree")
test_pascal2Camel(2, "1TwoThree", "1TwoThree")
test_pascal2Camel(3, "_TwoThree", "_TwoThree")
test_pascal2Camel(4, "'TwoThree", "'TwoThree")
test_pascal2Camel(5, "\nTwoThree", "\nTwoThree")
test_pascal2Camel(6, "oneTwoThree", "oneTwoThree")
