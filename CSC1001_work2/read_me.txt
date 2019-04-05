Q1£º
Input a positive number, then it will output the square root by sqrt().

Q2:
It generate a prime number list first(range from 2 to 9942, which is enough to generate 100 emirp number).
After that, it check every prime number in the list to determine whether it is an emirp number.
If ture, it will be appended to the emirp number list until we get 100 emirp numbers.
Final step is to print out the table.

Q3:
It use five functions:
legal_input(): the input should be all number and can't start with 4, 5, 6, 37.
isValid(): count the totalsum, if it%10 == 0, then it is valid.
sumofDoubleEvenPlace() and sumofDoubleOddPlace() are easy to read.
getDigit(): it adds every digit

Q4:
It sorts the string by letters order.

Q5:
False equals closed locker. Ture equals open one.
The strat point is student_num, and step is student_num+1.
Finally, it will print out the open locker numbers.

Q6:
It uses A[i], i to represent col and row.
It starts from 0 to test every position one by one. 
The queen shouldn't be put in the same col, row and diagonal.
If ture, it will continue to test next position.
If false(means that there is no position to put a queen in this row), it wil back to the last row to move to test next position.
When it has tested all eight rows, it will pick out a solution and the test will start from the next position.
Finally it will pick out all the solution.
It will randomly choose one solution from the total solution list to print out.
 


