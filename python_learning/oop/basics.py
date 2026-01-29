class User:
    company = "Elite"
    def __init__(self):
        self.name = input("Name: ")
        self.email = input("Email: ")
        self.phoneNo = input("Phone Number: ")
        self.age = input("Age: ")

    def printUserDetails(self):
        print(self.name, User.company, self.email, self.phoneNo, self.age)



def main():
    user = User()
    user.printUserDetails()

if __name__ == "__main__":
    main()
