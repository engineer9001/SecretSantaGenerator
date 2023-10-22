#Made by Dalton Myers in October 2023

import random
import os

def assign(inList, badPairs, badListCheck):
    """Takes a list of names, a list of tuples of bad pairs, and a bad list
    function. Randomly assigns each member of inList another member of inList
    as a dictionary where each value is the assignee and the key is the
    assignment. Then, passes the assignments and the badPairs variable
    to a function badListCheck that returns True if the pairings are
    unacceptable. If the pairings are unacceptable, recursively calls itself.
    If the pairings are acceptable, returns the dictionary of pairings.

    
    'There is absolutely no better way to do this' --Dustin Andree"""

    listLen = len(inList)
    if(listLen < 4):
        raise Exception('Input list is too short for a good secret santa. Find more friends :D')

    
    outlist = inList[:]
    random.shuffle(outlist)

    assignments = {k:v for (k,v) in zip(inList, outlist)}

    if badListCheck(assignments, badPairs):
        try:
            return assign(inList, badPairs, badListCheck)
        except:
            return assign(inList, badPairs, badListCheck)
    else:
        return assignments

def badList(assignments, badPairs):
    """Takes a dictionary of assignee:assignment and
    a list of tuples of unwanted assignment pairs and returns true
    if anyone is assigned to themselvesor any member of a bad pair
    has the other member of the baid pair (for couples) or any 'closed
    circuits of 2' (if x has y, y can't have x)"""
    for i in assignments:
        if assignments[i] == i:  #no one can have themselves
            return True
        if assignments[assignments[i]] == i:   #if x has y, y can't have x
            return True
    
    for i in badPairs:
        if assignments[i[0]] == i[1] or assignments[i[1]] == i[0]:   #couples
            return True


    return False
    

def writeFiles(assignments):
    """takes a dictionary of assignee:assignment and writes files
    as assignee.txt with the contents being the assignment. Includes 20
    empty lines for sending files through discord without them being visible
    to the sender."""
    newpath = "SecretSantaResults"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    for key in assignments:
        
        file = open(newpath + "/" + str(key) + ".txt", "w")
        file.write(20*'\n' + str(assignments[key]))
        file.close()

def main():

    inList = open('inList.txt').read().splitlines()
    badPairs = [(i.split()[0], i.split()[1]) for i in open('badPairs.txt', 'r').readlines()]

    
    for i in badPairs:  #make sure all entires in badList are also in inList and add them if they aren't and warn user
        for j in i:
            if j not in inList:
                print((str(j) + " is in badPairs.txt but not in inList.txt! ...adding for now, but this may be a mistake!!!"))
                inList.append(j)

    for i in inList:    #makes sure there are no duplicates in inList. Make the user fix them otherwise
        if inList.count(i) > 1:
            raise Exception("Duplicate names in inList. All names must be unique in inList.txt")


    assignments = assign(inList, badPairs, badList)   #DO IT!!!
    writeFiles(assignments)   #write the results to text files
    print(assignments)   #prototyping comment out before final run

if __name__ == '__main__':
    main()
