# Python-homework

This is one of the homework we did as a part of a college programming course. The text of the problem is:

Write a program that performs some processing on two files whose names are entered with
standard input and containing data on companies and auctions, respectively. **The company file row** contains information about **the company identifier (integer number), its name and the initial advertised price** (positive real number, maybe missing as
data, where the starting price is equal to 0). All data are separated by one comma (,). **The bidding file** contains information about the identifier of the company whose
value is bid, the amount of the bid (real number) and the name of the bidder. If the bid amount is not
a real number, signal error. All data are separated by exactly one blank character. Based on input files, **it is necessary to form a text file result.txt** which will
contain information about the companies after the auction. Each line of this file contains
data on one company, separated by exactly one blank character: company identifier,
its name and the initial advertised price, and for companies that had at least one offer and
the total number of valid bids, the last bid price and the name of the bidder of such price. Prices
print with 2 digits after the decimal point. A valid bid for the bidding company is the one whose
amount exceeds the last valid bid value for that company. Bids are listed
in chronological order, but not necessarily in ascending order (even for the same company).
The program should:
1) Load input file names.
2) Load data from specified files.
3) Perform the required processing according to the text of the task.
4) Form the output file according to the text of the task.
5) Take into account and process possible exceptions that may occur while performing the program.
