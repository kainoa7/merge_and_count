# Merge and Count

This repository contains an implementation of the merge and count algorithm in Python.

## Description

Merge and count is an algorithmic technique used to count the number of inversions in an array or sequence. An inversion occurs when two elements in a sequence are out of order with respect to each other. The merge and count algorithm efficiently counts inversions by merging two sorted halves of the sequence and counting inversions between elements from different halves.

The provided implementation of the merge and count algorithm recursively divides the input list into two halves, sorts and counts inversions in each half, merges the sorted halves while counting inversions, and returns the total number of inversions along with the sorted list.

## Implementation

The merge and count algorithm works as follows:

1. Divide the input list into two halves.
2. Recursively sort and count inversions in each half.
3. Merge the sorted halves while counting inversions between elements from different halves.
4. Return the total number of inversions and the sorted list.

## How to Use

To use this implementation of the merge and count algorithm, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the Python file.
4. Open a terminal or command prompt.
5. Run the following command to execute the script:

    ```
    python merge_and_count.py
    ```

6. The script will output the number of inversions in the input list and the sorted list.

## Example
- Takes a list of numbers: [3, 4, 5, 6, 2, 1, 3, 5]
- Returns the list in order as well as the inversions (number that is greater than the other other number)



