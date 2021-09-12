##def find(lst, s):
##    ''' find if a number is in a "twisted" list'''
##    n = len(lst)
##    if n == 1:
##        if s==lst[0]:
##            return 0
##        else:
##            return None
##    left = 0
##    right = n-1
##    middle = (left+right)//2
##    while right - left != 1: # find the 'switching' index
##        if lst[middle] > lst[left]:
##            left = middle
##            middle = (left+right)//2
##        else:
##            right = middle
##            middle = (left+right)//2
##    k = left
##    if s > lst[left] or (s<lst[right]): #then for sure the number ain't in the list
##        return None
##    left = 0 # first search - left of the list
##    right = k
##    middle = (left+right)//2
##    while right-left != 1 and right!=k:
##        if lst[middle] == s:
##            return middle #stop and we're done
##        if s > lst[middle]:
##            left = middle
##            middle =(left+right)//2
##        if s< lst[middle]:
##            right = middle
##            middle=(left+right)//2
##    if lst[left] == s: # cover case where number is at the leftmost
##        return left
##    left = k
##    right = n-1
##    middle = (left+right)//2  # second search - right of the list
##    while right-left != 1:
##        if lst[middle] == s:
##            return middle    #stop and we're done
##        if s > lst[middle]:
##            left = middle
##            middle =(left+right)//2
##        if s< lst[middle]:
##            right = middle
##            middle=(left+right)//2
##    if lst[right] == s: # cover case where number is at the rightmost
##        return right
##    return None
##
