"""
File: cashier.py
Author: Ken Lambert
"""

from linkedqueue import LinkedQueue

class Cashier(object):
    """Represents a cashier."""

    def __init__(self, id):
        """Maintains a queue of customers,
        number of customers served, total customer wait time,
        and a current customer being processed."""
        self.cashierID = id
        self.totalCustomerWaitTime = 0
        self.customersServed = 0
        self.currentCustomer = None
        self.queue = LinkedQueue()

    def addCustomer(self, c):
        """Adds an arriving customer to my line."""
        self.queue.add(c)
   
    def serveCustomers(self, currentTime):
        """Serves my cuatomers during a given unit of time."""
        if self.currentCustomer is None:
            # No customers yet
            if self.queue.isEmpty():
                return
            else:
                # Pop first waiting customer and tally results
                self.currentCustomer = self.queue.pop()
                self.totalCustomerWaitTime += \
                                            currentTime - \
                                            self.currentCustomer.getArrivalTime()
                self.customersServed += 1

        # Give a unit of service
        self.currentCustomer.serve()

        # If current customer is finished, send it away   
        if self.currentCustomer.getAmountOfServiceNeeded() == 0:
            self.currentCustomer = None
   
    def __str__(self):
        """Returns my results: my total customers served,
        my average wait time per customer, and customers left on my queue."""

        #result = "TOTALS FOR THE CASHIER\n" + \
        #         "Number of customers served:        " + \
        #         str(self.customersServed) + "\n"

        #if self.customersServed != 0:
        #    aveWaitTime = self.totalCustomerWaitTime /\
        #                  self.customersServed
        #    result += "Number of customers left in queue: " + \
        #              str(len(self.queue)) + "\n" + \
        #              "Average time customers spend\n" + \
        #              "waiting to be served:              " + \
        #              "%5.2f" % aveWaitTime
        if self.customersServed != 0:
            aveWaitTime = self.totalCustomerWaitTime /\
                          self.customersServed
        else:
            aveWaitTime = 0

        result = "  %2d       %2d         %5.2f       %2d" % (self.cashierID, self.customersServed, aveWaitTime, len(self.queue))  
        return result #FIXME: Keep an eye on the changes in this line
