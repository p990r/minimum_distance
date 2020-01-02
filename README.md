# Minimum Distance Codility challenge solved in Python

Integer V lies strictly between integers U and W if U < V < W or if U > V > W.

A non-empty zero indexed array A consisting of N integers is given.

A pair of indices (P, Q), where 0 ≤ P < Q < N is said to have adjacent values if no value in the array lies strictly between values A[P] and A[Q].

For example, in array A such that:

A[0] = 0

A[1] = 3

A[2] = 3

A[3] = 7

A[4] = 5

A[5] = 3

A[6] = 11

A[7] = 1


The following pairs of indices have adjacent values:

(0, 7),   (1, 2),   (1, 4),   (1, 5),   

(1, 7),   (2, 4),   (2, 5),   (2, 7),

(3, 4),   (3, 6),   (4, 5),   (5, 7).


For example,  indices 4 and 5 have adjacent values because there is no value in array A that lies strictly between
A[4] = 5 and A[5] =3; the only such value could be the number 4, and it is not present in the array.

Now, Find the distances among all adjacent pairs in the array.

A[0] = 0 and A[7] = 1, the distance between these indices is 7-0 = 7

A[1] = 3 and A[2] = 3, the distance between these indices is 2-1 = 1

A[1] = 3 and A[4] = 5, the distance between these indices is 4-1 = 3

A[1] = 3 and A[5] = 3, the distance between these indices is 5-1 = 4

A[1] = 3 and A[7] = 1, the distance between these indices is 7-1 = 6

A[2] = 3 and A[4] = 5, the distance between these indices is 4-2 = 2

A[2] = 3 and A[5] = 3, the distance between these indices is 5-2 = 3

A[2] = 3 and A[7] = 1, the distance between these indices is 7-2 = 5

A[3] = 7 and A[4] = 5, the distance between these indices is 4-3 = 1

A[3] = 7 and A[6] = 11, the distance between these indices is 6-3 = 3

A[4] = 5 and A[5] = 3, the distance between these indices is 5-4 = 1

A[5] = 3 and A[7] = 1, the distance between these indices is 7-2 = 5


here, minimum distance is 1.

Find the minimum distance between the adjacent pairs in the given non-empty zero-indexed array.

Return -2 if there are no adjacent pairs

Return -1 if the distance is greater than 100M.
