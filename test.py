from queue import PriorityQueue
# we initialise the PQ class instead of using a function to operate upon a list.
customers = PriorityQueue()
customers.put(("Harry", "Harry"))
customers.put(("C", "Charles"))
customers.put(("R", "Riya"))
customers.put(("S", "Stacy"))
while customers:
    print(customers.get())
