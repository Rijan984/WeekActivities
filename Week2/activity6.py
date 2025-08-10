class userDetail:
    def __init__(self, text):
        self.text=text

    def updateAge(self, personal_details):
        if self.text=="yes":
            updateYourAge=input("Update your age: ")
            personal_details[1]=updateYourAge
         # detail = userDetail(updateAge)
            print(personal_details)


def main():
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    address = input("Please enter your address: ")
    personal_details=[name, age, address]
    updateAge= input("Do you want to update your age: ")
    # print("my age: ", personal_details)
    updateFunction = userDetail(updateAge)
    updateFunction.updateAge(personal_details)

    # if updateAge=="yes":
    #     updateYourAge=input("Update your age: ")
    #     personal_details[1]=updateYourAge
    #     # detail = userDetail(updateAge)
    # print(personal_details)


if __name__=="__main__":
    main()




        
