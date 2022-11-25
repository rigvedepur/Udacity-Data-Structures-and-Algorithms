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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

tel_numbers = []

for record in texts:
    from_num, recieve_num = record[0], record[1]
    if from_num not in tel_numbers:
        tel_numbers.append(from_num)
    if recieve_num not in tel_numbers:
        tel_numbers.append(recieve_num)

for record in calls:
    from_num, recieve_num = record[0], record[1]
    if from_num not in tel_numbers:
        tel_numbers.append(from_num)
    if recieve_num not in tel_numbers:
        tel_numbers.append(recieve_num)


print(f'There are {len(tel_numbers)} different telephone numbers in the records.')