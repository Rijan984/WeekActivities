class StringManipulator:
    def __init__(self, text):
        self.text = text
        

    def find_character(self, char):
        return self.text.find(char)
    

name = StringManipulator("example")


result = name.find_character('x')
print("My lenght is:", len(name.text))
print("UpperCase:", name.text.upper() )
print(result)
# print("length is:", lenName)