
class numWord:
    def __init__(self, userWord):
        self.userWord=userWord
    def lenWord(self):
        return len(self.userWord)


def main():
    userWord = str(input("Please enter a word: "))
    name=numWord(userWord)

    print(len(userWord))
    print("The length of the word is: ", name.lenWord())

if __name__=="__main__":
    main()