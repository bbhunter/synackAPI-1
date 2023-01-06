#!/usr/bin/env python3

from synack import synack
import csv

s1 = synack()
s1.gecko = False
s1.Proxy = True
s1.getSessionToken()

def print_income(dct):
    for year, amount in dct.items():
        print("{}: ${:,.2f}".format(year, amount))

payouts = s1.getTransactions()
keys = payouts[0].keys()
transactionDict = dict()
for i in range(len(payouts)):
    thisYear = str(payouts[i]['transactionDate'][0:4])
    thisAmount = float(payouts[i]['amount'])
    if thisYear in transactionDict:
        tmpVal = transactionDict[thisYear]
        transactionDict[thisYear] = float(tmpVal) + float(thisAmount)
    else:
        transactionDict[thisYear] = float(thisAmount)
print_income(transactionDict)
