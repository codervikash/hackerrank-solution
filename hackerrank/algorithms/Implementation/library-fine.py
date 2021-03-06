""" Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0)fine=0).
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15 Hackos × (the number of days late)fine=15 Hackos × (the number of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500 Hackos × (the number of months late)fine=500 Hackos × (the number of months late).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos10000 Hackos.
Input Format

The first line contains 33 space-separated integers denoting the respective dayday, monthmonth, and yearyear on which the book was actually returned.
The second line contains 33 space-separated integers denoting the respective dayday, monthmonth, and yearyear on which the book was expected to be returned (due date).

Constraints

1≤D≤311≤D≤31
1≤M≤121≤M≤12
1≤Y≤30001≤Y≤3000
It is guaranteed that the dates will be valid Gregorian calendar dates.It is guaranteed that the dates will be valid Gregorian calendar dates.
Output Format

Print a single integer denoting the library fine for the book received as input.

Sample Input

9 6 2015
6 6 2015
Sample Output

45
"""

d1, m1, y1 = raw_input().strip().split(' ')
d1, m1, y1 = [int(d1), int(m1), int(y1)]
d2, m2, y2 = raw_input().strip().split(' ')
d2, m2, y2 = [int(d2), int(m2), int(y2)]

if y1 > y2:
    print 10000
elif m1 > m2 and y1 >= y2:
    print 500 * (m1 - m2)
elif d1 > d2 and m1 >= m2 and y1 >= y2:
    print 15 * (d1 - d2)
else:
    print 0
