#!/usr/bin/env python

import random


class Email:

    defaultpasswordlength = 10
    company_url = "company.com"
    emailcapacity = 500

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.password = Email._randompassword(self)
        self.department = Email._setdepartment(self)
        self.emailcapacity = Email.emailcapacity
        self.email = str(firstname + "." + lastname + "@" + self.department + "." + Email.company_url)

    def _randompassword(self):
        char = "ABCDEFHIJKLMNOPQRSTUVWXYZ%$!@"
        password = ""
        for i in range(Email.defaultpasswordlength):
            password += (char[random.randint(0, len(char) - 1)])
        return password

    def _setdepartment(self):
        print("Employee Name: " + self.firstname + " " + self.lastname +
              "\nPlease select department from list below:\n\n" +
              "1 for Sales\n" +
              "2 for Accounting\n" +
              "3 for Development\n" +
              "0 for None\n")
        depchoice = int(input("Department No: "))
        while True:
            if -1 < depchoice < 4:
                if depchoice == 1:
                    return "sales"
                    break
                elif depchoice == 2:
                    return "acct"
                    break
                elif depchoice == 3:
                    return "dev"
                    break
                else:
                    return ""
                    break
            else:
                print("Invalid input please try again.\n")
                depchoice = input("Department No: ")
                continue

    def setalternateemail(self, email):
        self.email = email

    def setpassword(self, password):
        self.password = password

    def show_info(self):
        return "DISPLAY NAME: " + self.firstname + " " + self.lastname + "\nCompany Email: " + self.email + "\nEmail Capacity: " + str(self.emailcapacity) + "mb\nPassword: " + str(self.password)
