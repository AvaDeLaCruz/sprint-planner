#!/bin/python3

import math
import os
import random
import re
import sys
from queue import PriorityQueue

# i'm using this challenge as an opportunity to get more practice with python (i'm pretty new to it!) so i'll be linking the resources i used for future reference in the comments

# https://www.w3schools.com/python/python_classes.asp
# https://www.programiz.com/python-programming/class


class Ticket:
    def __init__(self, ticketID, description, teamID, priority):
        self.ticketID = ticketID
        self.description = description
        self.teamID = teamID
        self.priority = priority
        self.sprintID = None

    def assignSprintID(self, sprintID):
        self.sprintID = sprintID


def writeResults():
    return None


def assignTickets(numTeams, numSprints, numTickets, ticketList, ticketPQ):
    return None


def parseAndStoreTicketData():
    return [], None


def parseNumberInputs():
    # https://www.journaldev.com/32137/read-stdin-python
    numTeams = input()
    numSprints = input()
    numTickets = input()
    return numTeams, numSprints, numTickets


def main():
    # https://realpython.com/python-pass-by-reference/
    # instead of passing vars by reference, return multiple vars
    numTeams, numSprints, numTickets = parseNumberInputs()

    # test = Ticket(1, 'hey there', 4, 'HIGH')
    # https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
    # print current attributes and values of obj
    # print(test.__dict__)

    ticketList, ticketPQ = parseAndStoreTicketData()
    # assignTickets(numTeams, numSprints, numTickets, ticketList, ticketPQ)
    # writeResults()
    return 1


if __name__ == '__main__':
    main()
    # Write your code here
