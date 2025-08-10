class empData:
    def __init__(self, fstEmpData, sndEmpData):
        self.fstEmpData=fstEmpData
        self.sndEmpData=sndEmpData

    def emp1Detail(self):
        emp1_name=input("Please enter first employee name: ")
        emp1_salary=int(input("Please enter first employee salary: "))
        emp1_jobTitle=input("Please enter first employee job title: ")

        self.fstEmpData=[emp1_name, emp1_salary, emp1_jobTitle]
        return self.fstEmpData

    def emp2Detail(self):
        emp2_name=input("Please enter second employee name: ")
        emp2_salary=int(input("Please enter second employee salary: "))
        emp2_jobTitle=input("Please enter second employee job title: ")

        self.sndEmpData=[emp2_name, emp2_salary, emp2_jobTitle]
        return self.sndEmpData

    def display_info(self):
        print(f"empName:{self.fstEmpData[0]}, salary:{self.fstEmpData[1]}, jobTitle:{self.fstEmpData[2]}")
        print(f"empName:{self.sndEmpData[0]}, salary:{self.sndEmpData[1]}, jobTitle:{self.sndEmpData[2]}")

    def give_raise(self, increaseSalary):
        self.fstEmpData[1] += increaseSalary
        self.sndEmpData[1] += increaseSalary
        print(f"Salary of {self.fstEmpData[0]} raised by {increaseSalary}, new salary is={self.fstEmpData[1]}")
        print(f"Salary of {self.sndEmpData[0]} raised by {increaseSalary}, new salary is={self.sndEmpData[1]}") 


def main():
    fstEmpData=[]
    sndEmpData=[]

    emp1Data=empData(fstEmpData, sndEmpData)
    firstEmp = emp1Data.emp1Detail()
    secondEmp = emp1Data.emp2Detail()
    
    print("Employer Details")
    emp1Data.display_info()

    increaseSalary = int(input("Enter the salary amount you want to increase: "))
    emp1Data.give_raise(increaseSalary)
    
    print("Employer Updated Details")
    emp1Data.display_info()


if __name__=="__main__":
    main()