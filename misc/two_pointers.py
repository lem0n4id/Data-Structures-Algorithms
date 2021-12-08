'''
Given a sorted array A (sorted in ascending order), 
having N integers, find if there exists 
any pair of elements (A[i], A[j]) 
such that their sum is equal to X.
'''

'''
The algorithm basically uses the fact that 
the input array is sorted. 

1. We start the sum of extreme values 
and conditionally move both pointers. 

2. We move left pointer ‘i’ when 
the sum of A[i] and A[j] is less than X. 

We do not miss any pair because the 
sum is already smaller than X. 

Same logic applies for right pointer j.'''


def naïveMethod(array:list, N:int, X:int):
    '''
        Time Complexity:  O(n^2).
    '''
    for i in range(N):
        for j in range(N):
 
            # as equal i and j means same element
            if(i == j):
                continue
 
            # pair exists
            if (array[i] + array[j] == X):
                return True
 
            # as the array is sorted
            if (array[i] + array[j] > X):
                break
             
    # No pair found with given sum
    return False

def twoPointerMethod(array:list, N:int, X:int):
    """
        Time Complexity:  O(n).
    """
 
    # represents first pointer
    i = 0
 
    # represents second pointer
    j = N - 1
 
    while(i < j):
       
        # If we find a pair
        if (array[i] + array[j] == X):
            return True
 
        # If sum of elements at current
        # pointers is less, we move towards
        # higher values by doing i += 1
        elif(array[i] + array[j] < X):
            i += 1
 
        # If sum of elements at current
        # pointers is more, we move towards
        # lower values by doing j -= 1
        else:
            j -= 1
    return False


print(naïveMethod([10, 20, 35, 50, 75, 80], 6, 70))
print(naïveMethod([10, 20, 35, 50, 75, 80], 6, 70))