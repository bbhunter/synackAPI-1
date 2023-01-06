#!/usr/bin/env python3

from synack import synack
import csv

s1 = synack()
s1.gecko = False
s1.Proxy = True
s1.getSessionToken()

fields = ['Date', 'Payout']
payouts = s1.getTransactions()
with open('synack_payouts.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(payouts)
