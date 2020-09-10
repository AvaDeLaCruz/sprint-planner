#!/bin/python3

import math
import os
import random
import re
import sys
from queue import PriorityQueue

# i'm using this challenge as an opportunity to get more practice with python (i'm pretty new to it!) so i'll be linking the resources i used for future reference in the comments


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
    print(numTeams, numSprints, numTickets)
    # ticketList, ticketPQ = parseAndStoreTicketData()
    # assignTickets(numTeams, numSprints, numTickets, ticketList, ticketPQ)
    # writeResults()
    return 1


if __name__ == '__main__':
    main()
    # Write your code here
