# SecretSantaGenerator
A python script that takes in a list of participants and a list of unwanted secret santa pairings as text files, and outputs one text file named for the assignee per participant with the contents of that text file being the assignment for the person.

The purpose of this script is to allow a participant in the secret santa to also be the person who sends out assignments wihtout knowing the assignment of each person.
Simply message each participant the file called "participant.txt" and only ever look at the one that is called "your_name.txt"

Included are some example lists of the required formatting, but inList.txt must be a text file with one name per line and the names must be unique (and no spaces!). badList.txt should have two names per line seperated by a semi-colon. The purpose of bad pairs is to make sure any undesired pairings won't appear in the final secret santa list. Especially useful to mkae sure no one in a participating couple gets assigned their partner.
