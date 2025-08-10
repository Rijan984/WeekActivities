class StringManipulator:
    def __init__(self, text):
        self.text = text

    def find_character(self, char):
        return self.text.find(char)
    
    def lenFind(self):
        return len(self.text)
    
    def upper_case(self):
        return self.text.upper()
    

name = StringManipulator("example")


result = name.find_character(text="example", char='x')
print("My lenght is:", name.lenFind())
print("UpperCase:", name.upper_case() )

# print("My lenght is:", len(name.text))
# print("UpperCase:", name.text.upper() )
print(result)