# Train ticket booking system using python classes and objects by Chirantan Banerjee
'''
This is a train ticket booking system.
Logic used - Suppose a train has 5 seats [1,2,3,4,5]  so when a train ticket is booked it will reduce one seat 
from the list for which i used pop() function.Again if someone will cancel his seat it the reduced seat will be
added back to the list for which i used the append function.

'''
class Train :
    def __init__(self,name,seats,fair):
        self.name = name
        self.seats = seats
        self.fair = fair
    def getstatus(self): 
        print(f"NAME OF THE TRAIN {self.name} || SEATS STATUS : AVAILABLE SEATS  {len(self.seats)} || TRAIN FARE Rs {self.fair}")
        print("-------------------------------------------------------------------------------------------------")
    def booktickets(self):
        if len(self.seats) > 0 :
            print(f"CONGRATULATIONS YOUR SEATS ARE BOOKED")
            print("-------------------------------------------------------------------------------------------------")
            self.seats.pop()
        else :    
            print("SEATS NOT AVAILABLE ASK TICKET DEPARTMENT FOR ALTERNATIVES")
            print("-------------------------------------------------------------------------------------------------")
    def ticketCancellation(self,num):
        self.seats.append(num)
        print(f"CONFIRMATION ! YOUR SEATS ARE CANCELLED SEAT NO. CANCELLED {num}")

# Checking the programme works or not 
nilgiriexpress = Train("Nilgiri Express",[1,2,3,4,5,6,7,8,9,10],500) #Give parameters to the instance
nilgiriexpress.getstatus()  #Know the status
nilgiriexpress.booktickets() #One ticket booked
nilgiriexpress.getstatus() #Check status one seat reduced from the list 
nilgiriexpress.ticketCancellation(10) #Seat added after cancellation
nilgiriexpress.getstatus() #Check status seats added






               

