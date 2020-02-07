"""
File: marketmodel.py
"""

from cashier import Cashier
from customer import Customer
from random import randint
from random import seed

class MarketModel(object):

    def __init__(self, lengthOfSimulation, averageTimePerCus,
                 probabilityOfNewArrival, cashierCount):
        self.probabilityOfNewArrival = probabilityOfNewArrival
        self.lengthOfSimulation = lengthOfSimulation
        self.averageTimePerCus = averageTimePerCus
        self.cashierCount = cashierCount
        self.cashier = []
        for count in range(0, self.cashierCount):
            self.cashier.append(Cashier(count + 1))
   
    def runSimulation(self):
        """Run the clock for n ticks."""
        seed(3)
        for currentTime in range(self.lengthOfSimulation):
            # Attempt to generate a new customer
            customer = Customer.generateCustomer(
                self.probabilityOfNewArrival,
                currentTime,
                self.averageTimePerCus)

            # Send customer to cashier if successfully generated
            cashier = randint(1, self.cashierCount)
            if customer != None: 
                self.cashier[cashier - 1].addCustomer(customer) 
                #self.cashier.addCustomer(customer) #Removed as the preceding line replaced

            # Tell cashier to provide another unit of service
            for rep in self.cashier:
                rep.serveCustomers(currentTime) #FIXME: Keep an eye on the changes in this line

    def __str__(self):
        print("CASHIER CUSTOMERS   AVERAGE     LEFT IN ")
        print("        PROCESSED   WAIT TIME   LINE    ")
        for count in self.cashier:
            print(count)

        return ""
        #return str(self.cashier) #FIXME: must return more than one cashier? Check the canvas page, return the multiple cashier strings
