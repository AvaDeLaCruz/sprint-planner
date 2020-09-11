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


def parseAndStoreTicketData(numTickets):
    # https://stackoverflow.com/questions/8162021/analyzing-string-input-until-it-reaches-a-certain-letter-on-python
    # https://docs.python.org/2/library/stdtypes.html#str.partition
    # https://www.w3schools.com/python/python_for_loops.asp
    ticketList = []
    for line in sys.stdin:
        ticketData = []
        partitionTuple = line.partition("/ ")
        # while the partitioned string before target sequence is not empty
        # aka while there is still ticket data to add
        while partitionTuple[0] != '':
            ticketData.append(partitionTuple[0])
            line = partitionTuple[2]
            partitionTuple = line.partition("/ ")

        ticket = Ticket(int(ticketData[0]), ticketData[1], int(
            ticketData[2]), ticketData[3].rstrip())
        ticketList.append(ticket)

    return ticketList, None


def parseNumberInputs():
    # https://www.journaldev.com/32137/read-stdin-python
    # https://realpython.com/convert-python-string-to-int/
    numTeams = int(input())
    numSprints = int(input())
    numTickets = int(input())
    return numTeams, numSprints, numTickets


def main():
    # https://realpython.com/python-pass-by-reference/
    # instead of passing vars by reference, return multiple vars
    numTeams, numSprints, numTickets = parseNumberInputs()

    # https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
    # print current attributes and values of obj
    # test = Ticket(1, 'hey there', 4, 'HIGH')
    # print(test.__dict__)
    # test.assignSprintID(9)
    # print(test.__dict__)

    ticketList, ticketPQ = parseAndStoreTicketData(numTickets)

    for ticket in ticketList:
        print(ticket.__dict__)

    # assignTickets(numTeams, numSprints, numTickets, ticketList, ticketPQ)
    # writeResults()
    return 1


if __name__ == '__main__':
    main()
    # Write your code here
