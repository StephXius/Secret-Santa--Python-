import smtplib
from privacy import sender
from privacy import password
import email
import random


class SecretSanta:

    def __init__(self):
        self.info = dict()
        self.selection = dict()
        self.participants = 0
        self.budget = 0

    def get_info(self):
        self.participants = int(input("How many people are participating in Secret Santa?: "))
        self.budget = int(input("What is the budget for this Secret Santa?"))

        for i in range(1, self.participants + 1):
            name = input("What is the name of the participant {}?: ".format(i))
            email - input("What is their email?: ")
            address = input("What is their address?: ")
            request = input("What is their gift request? (seperated by commas): ")
            self.info[name] = [email, address, request]

    def assign(self):
        choices = [name for name in self.info]

        for person in self.info:
            secret_person = random.choice(choices)
            while secret_person == person or secret_person in self.selection:
                secret_person = random.choice(choices)
            if secret_person in self.selection and self.selection[secret_person] == person:
                continue
            elif secret_person == person:
                continue
            break
        self.selection[person] = secret_person
        ind = choices.index(secret_person)
        choices.pop(ind)

    def send_emails(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        print("Login Successful.")
        for person,sp in self.selection.items():
            receiver = self.info[person][0]
            sp_address = self.info[sp][1]
            sp_request = self.info[sp][2]
            message = "SUBJECT: SECRET SANTA\n" \
                      "Hello {}, \n\n" \
                      "Shhhh, your secret santa person this year is: {}. \n\n" \
                      "The budget of the gift exchange is: ${}. \n\n" \
                      "Here is {}'s wishlist: {}\n\n" \
                      "This is the address for the gift exchange: {}\n\n" \
                      "Thanks for participating in this year Secret Santa!".format(person,sp,self.budget,sp,sp_request,sp_address) 
            server.sendmail(sender, receiver, message)
            print("{} has been sent their secret person".format(person))
            server.quit()


    def start(self):
        self.get_info()
        self.assign()
        self.send_emails()

if __name__ == '__main__':
    secret_santa = SecretSanta()
    secret_santa.start()