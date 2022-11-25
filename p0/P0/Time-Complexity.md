# Time Complexity Analysis for Tasks


## Task 0

The code in Task 0 will run only one time regardless of the size of input. Therefore,
#### <b>Run time complexity is O(0n)--> O(1)</b>

## Task 1

For each task (texts and calls), the program needs to iterate through all the numbers one at a time.

#### <b>Run time complexity is O(n+n)--> O(2n)--> O(n)</b>

## Task 2

For each call record, there are multiple computations such as
* check if both 'from' and 'to' numbers are already present
* If number is already present, then add keep adding call time
* keep track of max time and update if call time for current record exceeds max time

All these computations occur only once per call record.

Therefore,
#### <b>Run time complexity = O(n)</b>

## Task 3

There are 2 for loops in this program (Part A & Part B)

<b>Part A:</b>

In first for loop, following computations are performed:
* check if 'from' number is (080)
* if receiving number is a landline or a mobile number (has an empty space after first 4 digits)
* further check in the receiving numbers if they are from Bangalore (080)
* Sort all receiving numbers and print them one at a time. Time complexity for sort algorithm is nlog(n)


All these steps are computed once for an input.
#### <b>Run time complexity for part A = O(n + nlogn) </b>

<b>Part B:</b>

In part B, the calls for fixed lien in Bangalore are already calculated in Part A. Therefore total run time complexity is still
#### <b> O(n + nlogn) </b>



## Task 4

There are 3 main loops in this Task

* In first loop, the program iterates over all texts. Run time complexity is O(n)
* In second loop, the program iterates over all calls. Run time complexity is O(n)
* The third loop is a sort loop. The run time complexity is O(nlogn)

Adding all these,

#### <b>Total Run time complexity = O(n + n + nlogn)
#### = O(2n +nlogn) </b>
