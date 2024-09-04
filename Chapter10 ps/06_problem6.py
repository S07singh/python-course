from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo =trainNo

    def book(sudhir, fro, to):
        print(f"Ticked is booked in train no: {sudhir.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")

# if we change the self word to slf or sudhir, nothing will happen 
#program will run without any problem