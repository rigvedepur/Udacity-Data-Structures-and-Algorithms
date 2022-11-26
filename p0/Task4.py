"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_senders_receivers = []

for record in texts:
    sender, receiver = record[0], record[1]
    if (sender not in text_senders_receivers):
        text_senders_receivers.append(sender)
    if (receiver not in text_senders_receivers):
        text_senders_receivers.append(receiver)

telemarketers = []
number_to_avoid = []
receivers = []

for record in calls:
    caller, receiver = record[0], record[1]
    number_to_avoid.append(receiver)

for record in calls:
    caller, receiver = record[0], record[1]
    if (caller in text_senders_receivers) or (caller in telemarketers) or (caller in number_to_avoid):
        continue
    else:
        telemarketers.append(caller)

for number in sorted(telemarketers):
    print(number)