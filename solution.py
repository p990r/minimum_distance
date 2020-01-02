def solution(A):
    if (len(A)<2):
        return -2

    A.sort()
    minDist = A[1]-A[0]

    for i in range(2,len(A)):
        dist = A[i] - A[i-1] # no need to use abs() since A is sorted
        if(dist<minDist):
            minDist = dist

    if(minDist>100000000):
        return -1
    return minDist
