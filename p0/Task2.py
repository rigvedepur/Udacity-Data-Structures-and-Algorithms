"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
number_time_dict = {}
max_time = 0

for record in calls:
    from_num, receive_num, time_spent = record[0], record[1], int(record[3])
    if from_num not in number_time_dict.keys():
        number_time_dict[from_num] = 0
    if receive_num not in number_time_dict.keys():
        number_time_dict[receive_num] = 0

    number_time_dict[from_num] += time_spent
    number_time_dict[receive_num] += time_spent

    if number_time_dict[from_num] > max_time:
        max_time = number_time_dict[from_num]
        max_time_number = from_num

    if number_time_dict[receive_num] > max_time:
        max_time = number_time_dict[receive_num]
        max_time_number = receive_num


print(f'{max_time_number} spent the longest time, {max_time} seconds, on the phone during September 2016')
