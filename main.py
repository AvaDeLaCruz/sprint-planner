#!/bin/python3

import math
import os
import random
import re
import sys
from queue import PriorityQueue

# i'm using this challenge as an opportunity to get more practice with python
# (i'm pretty new to it!) so i'll be linking the resources i used for future
# reference in the comments at the bottom of the file


class Ticket:
    priorities = {
        "HIGH": 0,
        "MED": 1,
        "LOW": 2
    }

    def __init__(self, ticketID, description, teamID, priority):
        self.ticketID = ticketID
        self.description = description
        self.teamID = teamID
        self.priority = priority
        self.priorityValue = self.priorities.get(priority)
        self.sprintID = None

    def assignSprintID(self, sprintID):
        self.sprintID = sprintID

    def __str__(self):
        ticketString = str(self.ticketID) + "/ " + self.description + \
            "/ " + str(self.teamID) + "/ " + self.priority
        if self.sprintID is not None:
            ticketString += "/ " + str(self.sprintID)
        return ticketString


def writeResults(assignedTickets, ticketList, numTickets):
    assignedTicketIDs = []
    while not assignedTickets.empty():
        ticketTuple = assignedTickets.get()
        ticket = ticketTuple[1]
        print(ticket)
        assignedTicketIDs.append(ticket.ticketID)
    unassignedTickets = [ticketList[i]
                         for i in range(numTickets) if i not in assignedTicketIDs]
    for ticket in unassignedTickets:
        print(ticket)

    return None


def assignTicketsToSprints(numSprints, teamsTicketsList):
    assignedTickets = PriorityQueue()
    for sprintNum in range(numSprints):
        for teamsTickets in teamsTicketsList:
            if not teamsTickets.empty():
                teamTuple = teamsTickets.get()
                ticket = teamTuple[1]
                ticket.assignSprintID(sprintNum)
                entry = ((sprintNum, ticket.ticketID), ticket)
                assignedTickets.put(entry)

    return assignedTickets


def sortTicketsByTeam(numTeams, numTickets, ticketList):
    teamsTicketsList = []
    for teamNumber in range(numTeams):
        teamPQ = PriorityQueue()
        teamsTicketsList.insert(teamNumber, teamPQ)
    for ticket in ticketList:
        # create an entry with priorityValue as the first priority
        # ticketID as the tiebreaker
        # and the Ticket object ticket
        ticketID = ticket.ticketID
        priorityValue = ticket.priorityValue
        entry = ((priorityValue, ticketID), ticket)
        # insert the entry into the PQ associated with the Ticket's team
        teamID = ticket.teamID
        teamPQ = teamsTicketsList[teamID]
        teamPQ.put(entry)

    return teamsTicketsList


def parseTicketData(numTickets):
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

    return ticketList


def parseNumberInputs():
    numTeams = int(input())
    numSprints = int(input())
    numTickets = int(input())

    return numTeams, numSprints, numTickets


def main():
    numTeams, numSprints, numTickets = parseNumberInputs()
    ticketList = parseTicketData(numTickets)
    teamsTicketsList = sortTicketsByTeam(numTeams, numTickets, ticketList)
    assignedTickets = assignTicketsToSprints(numSprints, teamsTicketsList)
    writeResults(assignedTickets, ticketList, numTickets)

    return 1


if __name__ == '__main__':
    main()


# learnings and resources
# https://stackoverflow.com/questions/192109/is-there-a-built-in-function-to-print-all-the-current-properties-and-values-of-a
# https://realpython.com/python-pass-by-reference/
# instead of passing vars by reference, return multiple vars
# https://www.journaldev.com/32137/read-stdin-python
# https://realpython.com/convert-python-string-to-int/
# https://docs.python.org/3.1/library/heapq.html#priority-queue-implementation-notes
# https://stackoverflow.com/questions/8162021/analyzing-string-input-until-it-reaches-a-certain-letter-on-python
# https://docs.python.org/2/library/stdtypes.html#str.partition
# https://www.w3schools.com/python/python_for_loops.asp
# https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
# https://dbader.org/blog/python-repr-vs-str
# https://www.geeksforgeeks.org/switch-case-in-python-replacement/
# https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3
# https://www.w3schools.com/python/python_classes.asp
# https://www.programiz.com/python-programming/class
