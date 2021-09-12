#Skeleton file for HW4 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to include your ID number (hw4_ID.py).


############
# QUESTION 2
############


# a
def win(n,m):
    if n==1 and m==1:  # base case
        return False
    for i in range(n-1, 0, -1): #reduce n
        if win(i,m) == False:
            return True
    for k in range(m-1, 0, -1): # reduce m
        if win(n,k) == False:
            return True
    return False # if no way for the win

# c
def win_fast(n,m):
    win_dict = {}
    return win2(n,m,win_dict)


def win2(n,m, win_dict):
    if n==1 and m==1:  # base case
        return False
    if (n,m) not in win_dict:
        for i in range(n-1, 0, -1):
            if win2(i,m, win_dict) == False:
                win_dict[(n,m)]= True # index in dict
                return win_dict[(n,m)] 
        for k in range(m-1, 0, -1):
            if win2(n,k,win_dict) == False:
                win_dict[(n,m)] = True   # index in dict
                return win_dict[(n,m)]
        win_dict[(n,m)] = False
        return win_dict[(n,m)]
    return win_dict[(n,m)]



############
# QUESTION 3
############

# b
def had_local(n, i, j):
    ''' finds the ith row, jth column number in Hadamard's n matrix '''
    if n==0: #base case
        return 0
    if i < 2**(n-1) and j<2**(n-1): #upper left
        return had_local(n-1, i, j)
    if i <2**(n-1) and j>=2**(n-1): #lower left
        return had_local(n-1, i, j-2**(n-1))
    if i>=2**(n-1) and j<2**(n-1): #upper right
        return had_local(n-1,i-2**(n-1),j)
    if i>=2**(n-1) and j>=2**(n-1):  #lower right
        return 1-had_local(n-1,i-2**(n-1), j-2**(n-1))

# d
had_complete = lambda n : \
               [[had_local(n,i,j) for j in range(2**n)] for i in range(2**n)]



############
# QUESTION 4
############

def subset_sum_count(L, s):
    if s==0 and 0 in L:
        return 2
    if s==0:
        return 1
    if L == []:
        return 0

    with_first = subset_sum_count(L[1:], s-L[0])
    without_first = subset_sum_count(L[1:], s)

    return with_first + without_first

def subset_sum_search_all(L, s):
    return subsets(L,s,[],[])

def subsets(L,s,new,aide=[]):
    if s==0:
        helpy = [i for i in aide]
        new.append(helpy)
        return [[]]
    if L==[]:
        return []
    
    aide.append(L[0])
    with_first = subsets(L[1:], s-L[0],new,aide)
    aide.pop()
    without_first = subsets(L[1:], s,new,aide)

    return new
            


############
# QUESTION 6
############

def distance(s1, s2):
    if len(s1)>=len(s2):
        return distance_calc(s1,s2,0)
    else:
        return distance_calc(s2,s1,0)
    

def distance_calc(s1,s2,collect):
    if s1=='':
        return len(s2)+collect #all previous changes + 'leftovers'
    if s2=='':
        return len(s1)+collect #all previous changes + 'leftovers'
    
    if s1[0]==s2[0]:
        return distance_calc(s1[1:],s2[1:],collect) #skip those letters and move on

    else:
        collect +=1 #we got inequality, so we count it
        first = distance_calc(s1[1:], s2[1:], collect) #to cover letter replacement
        second = distance_calc(s1[1:],s2,collect) # to cover letter drop in second word
        third = distance_calc(s2[0]+s1,s2,collect) # to cover letter addition in second word

        return min(first,second,third) # to avoid counting irrelevant cases

def distance_fast(s1, s2):
    dicty = {}
    if len(s1)>=len(s2):
        return distance_mem(s1,s2,0,dicty)
    else:
        return distance_mem(s2,s1,0,dicty)

def distance_mem(s1, s2,collect,dicty):
    if (s1, s2,collect) not in dicty:
        if s1=='':
            dicty[(s1,s2,collect)]=len(s2)+collect
            return dicty[(s1,s2,collect)] #all previous changes + 'leftovers'

        if s2=='':
            dicty[(s1,s2,collect)]=len(s1)+collect
            return dicty[(s1,s2,collect)] #all previous changes + 'leftovers'
    
        if s1[0]==s2[0]:
            dicty[(s1,s2,collect)]= distance_mem(s1[1:],s2[1:],collect,dicty) #skip those letters and move on
            return dicty[(s1,s2,collect)]
 
        else:
            collect +=1 #we got inequality, so we count it
            first = distance_mem(s1[1:], s2[1:], collect,dicty) #to cover letter replacement
            second = distance_mem(s1[1:],s2,collect,dicty) # to cover letter drop in second word
            third = distance_mem(s2[0]+s1,s2,collect,dicty) # to cover letter addition in second word

            dicty[(s1,s2,collect)]= min(first,second,third) # to avoid counting irrelevant cases
            return dicty[(s1,s2,collect)]
        
    return dicty[(s1,s2,collect)]


########
# Tester
########

def test():
    if win(3,3) != False or\
       win(3,4) != True or\
       win(1,1) != False or\
       win(1,2) != True :
        print("Error in win()")

    if win_fast(3,3) != False or \
       win_fast(3,4) != True or\
       win_fast(1,1) != False or\
       win_fast(1,2) != True :
        print("Error in win_fast()")

    contains = lambda L, R : all(R.count(r) <= L.count(r) for r in R)
    L = [1, 2, 4, 8, 16]

    if subset_sum_count(L, 13) != 1 or subset_sum_count(L, 32) != 0 \
       or subset_sum_count([i for i in range(1, 10)], 7) != 5:
        print("Error in subset_sum_count")

    R_lst = subset_sum_search_all(L, 13)
    if R_lst == None:
        print("Error in subset_sum_search_all")
    elif len(set([tuple(sorted(R)) for R in R_lst])) != len(R_lst) or len(R_lst) != 1:
        print("Error in subset_sum_search_all")
    else:
        for R in R_lst:
            if R == None or not sum(R) == 13 or not contains(L,R):
                print("Error in subset_sum_search_all")

    R_lst = subset_sum_search_all(L, 32)
    if not R_lst == []:
        print("Error in subset_sum_search_all")

    L = [i for i in range(1, 10)]
    R_lst = subset_sum_search_all(L, 7)
    if R_lst == None:
        print("Error in subset_sum_search_all")
    elif len(set([tuple(sorted(R)) for R in R_lst])) != len(R_lst) or len(R_lst) != 5:
        print("Error in subset_sum_search_all")
    else:
        for R in R_lst:
            if R == None or not sum(R) == 7 or not contains(L,R):
                print("Error in subset_sum_search_all")

    if distance('computer','commuter') != 1 or \
       distance('sport','sort') != 1 or \
       distance('','ab') != 2 or distance('kitten','sitting') != 3:
        print("Error in distance")

    if distance_fast('computer','commuter') != 1 or \
       distance_fast('sport','sort') != 1 or \
       distance_fast('','ab') != 2 or distance_fast('kitten','sitting') != 3:
        print("Error in distance_fast")

    
    
        
