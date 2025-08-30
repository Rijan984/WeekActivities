class user:
    def __init__(self, name, email, password):
        self.name=name #public
        self._email=email #protected
        self.__password=password #private

    def getPassword(self):
        return self.__password
    

def main():
    userDetail = user("Rijan", "rijan@gmail.com", "rijan12")
    print(userDetail.getPassword()) #correct way to access private attribute but cant access it using userDetail.__password
    print(userDetail.name)
    print(userDetail._email) #accessible but not the correct way
    

if __name__ == "__main__":
    main()