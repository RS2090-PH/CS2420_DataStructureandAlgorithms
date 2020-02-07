"""
Modify the supermarket checkout simulator so that it simulates a store with many checkout lines.

Add the number of cashiers as a new user input.

At instantiation, the model should create a list of these cashiers. When a customer is generated, it 
should be sent to a cashier randomly chosen from the list of cashiers. On each tick of the abstract 
clock, each cashier should be told to serve its next customer. At the end of the simulation, the 
results for each cashier should be displayed.

You will need to modify several files in this project.
"""