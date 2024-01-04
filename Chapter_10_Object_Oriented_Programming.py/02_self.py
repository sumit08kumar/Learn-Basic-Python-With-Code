class Employee:
    company = "Google"
    def getsalary(self):
        print(f"Salary is for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100100
harry.getsalary()
