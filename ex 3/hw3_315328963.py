# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).


import random


############
# QUESTION 2
############

def cycle(n):
    mat = [] # creating the matrix
    draft = [0 for i in range(n)]
    first_row = [0 for i in range(n)] 
    first_row[1] = 1
    first_row[n-1] = 1
    mat.append(first_row) # handle first special case
    for i in range(1,n-1): # handle regular cases
        new_list = [0 for i in range(n)]
        new_list[i-1] = 1
        new_list[i+1] = 1
        mat.append(new_list)
    last_row = [0 for i in range(n)]
    last_row[0] = 1
    last_row[n-2] = 1
    mat.append(last_row) # handle second special case
    return mat

def complete_graph(n):
    any_row = [1 for i in range(n)]
    mat = [any_row for i in range(n)]
    return mat

def random_graph(n, p):
    my_list = [0, 1] # options
    mat = [random.choices(my_list, [1-p, p] , k=n) for k in range(n)] #defines each row
    return mat

def inv_cycle(n):
    mat = [] # creating the matrix
    draft = [0 for i in range(n)]
    first_row = [0 for i in range(n)] 
    first_row[0:2] = 1, 1 #refering to opposite element
    first_row[n-1] = 1
    mat.append(first_row) # handle first special case
    for i in range(1,n-1): # handle regular cases
        new_list = [0 for i in range(n)]
        opposite = i**(n-2) % n #refering to opposite element
        new_list[i-1] = 1
        new_list[i+1] = 1
        new_list[opposite] = 1
        mat.append(new_list)
    last_row = [0 for i in range(n)]
    opposite = (n-1)**(n-2) % n #refereing to opposite element
    last_row[0] = 1
    last_row[n-2] = 1
    last_row[opposite]= 1
    mat.append(last_row) # handle second special case
    return mat

def return_graph(n):
    mat = []
    draft = [0 for k in range(n)]
    first_row = [0 for k in range(n)]
    first_row[1] = 1     #only one condition applies
    mat.append(first_row)
    for i in range(1, n-1):
        new_list = [0 for k in range(n)] # handle both conditions
        new_list[i+1] = 1
        new_list[0] = 1
        mat.append(new_list)
    last_row = [0 for k in range(n)]
    last_row[0] = 1    #only one condition applies
    mat.append(last_row)
    return mat

def random_step(adj, v):
    node = adj[v] # chosen node
    options = []
    for i in range(len(node)): # creating list of relevant choices
        if node[i] == 1:
            options.append(i)
    choice = random.choice(options)
    return choice

def walk_histogram(adj):
    histogram = [0 for i in range(len(adj))] # create the histogram
    histogram[0]=1 # first 'step'
    step = random_step(adj, 0)
    histogram[step]+=1
    checking = step # our 'barrier'
    while checking < sum(range(len(adj))):
        step = random_step(adj, step) # update step
        histogram[step]+=1
        if histogram[step] == 1: #to avoid repeating the checking
            checking += step
    return histogram

def cover_time(adj):
    return sum(walk_histogram(adj))

############
# QUESTION 3
############

# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selection_sort(lst):
    """ sort lst (in-place) """
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None


def generate_sorted_blocks(lst, k):
    new_list = []
    for i in range(1, len(lst)//k+1):
        temp = lst[(i-1)*k:i*k]
        sort = selection_sort(temp)
        if sort == None:
            new_list.append(temp)
        else:
            new_list.append(sort)
    less = len(lst) % k
    if less != 0:
        last= lst[len(lst)-less:]
        sort = selection_sort(last)
        if sort == None:
            new_list.append(last)
        else:
            new_list.append(sort)
    return new_list


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


# c
def merge_sorted_blocks(lst):
    while len(lst) != 1:
        aide = [] # to help minimize lst
        for i in range(0, len(lst), 2):
            if i == len(lst)-1: # cover cases where lst length is odd
                aide.append(lst[i])
                break
            aide.append(merge(lst[i], lst[i+1]))
        lst = aide
    return lst[0] #the relvant and only item


def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find_missing(lst, n):
    left = 0
    right = n-1
    middle = (left+right)//2
    if lst[n-1] == n-1: # cover immediate case where last one missing
        return n
    while (right - left)!=1: #we stop when the indexes are by each other to check if condition applies
        if lst[middle] == middle: 
            left = middle
            middle = (left+right)//2 #go towards right - search for disrepancy with index
        else:
            right = middle # go towards left - search for match with index
            middle = (left+right)//2
    if lst[right] == right+1 and lst[left] == left:
            return right #the only other option is the base case covered above


def find(lst, s):
    ''' find if a number is in a "twisted" list'''
    n = len(lst)
    if n == 1:
        if s==lst[0]:
            return 0
        else:
            return None
    left = 0
    right = n-1
    middle = (left+right)//2
    while right - left != 1: # find the 'switching' index
        if lst[middle] > lst[left]:
            left = middle
            middle = (left+right)//2
        else:
            right = middle
            middle = (left+right)//2
    if s > lst[left] or (s<lst[right]): #then for sure the number ain't in the list
        return None
    k = left
    left = k+1-n
    right = k
    middle=(left+right)//2
    while right-left!=1:
        if s==lst[middle]:
            if middle<0:
                return n+middle
            else:
                return middle
        if s>lst[middle]:
            left=middle
            middle=(left+right)//2
        if s<lst[middle]:
            right=middle
            middle=(left+right)//2
    if lst[right] ==s:
        if right <0:
            return n+right
        else:
            return right
    if lst[left]==s:
        if left<0:
            return n+left
        else:
            return left
    return None


def find2(lst, s):
    n = len(lst)
    collection = []
    change = -1
    if n == 1:
        if s==lst[0]:
            return 0
        else:
            return None
    left = 0
    right = n-1
    middle = (left+right)//2
    while right-left!=1:
        if lst[middle-1] > lst[middle]:
            change = middle-1
            break
        if lst[middle+1] < lst[middle]:
            change = middle
            break
        collection.append(middle)
        left = middle
        middle = (left+right)//2
    if change == -1:
        left = 0
        right = n-1
        middle = (left+right)//2
        while right-left != 1:
            if lst[middle-1] > lst[middle]:
                change = middle-1
                break
            if lst[middle+1] < lst[middle]:
                change = middle
                break
            collection.append(middle)
            right = middle
            middle = (left+right)//2
    if change == -1:
        for i in range(len(lst)):
            if lst[i] == s:
                return i
        else:
            return None
    if s > lst[change] or (s<lst[change]): #then for sure the number ain't in the list
        return None
    k = change
    left = k+1-n
    right = k
    middle=(left+right)//2
    while right-left!=1:
        if s==lst[middle]:
            if middle<0:
                return n+middle
            else:
                return middle
        if s>lst[middle]:
            left=middle
            middle=(left+right)//2
        if s<lst[middle]:
            right=middle
            middle=(left+right)//2
    if lst[right] ==s:
        if right <0:
            return n+right
        else:
            return right
    if lst[left]==s:
        if left<0:
            return n+left
        else:
            return left
    return None




############
# QUESTION 5
############

# a
def string_to_int(s):
    dicty = {"a":0, "b":1, "c":2, "d":3, "e":4}
    summing = 0
    for i in range(-1, -len(s)-1, -1):
        summing += 5**(abs(i)-1)*dicty[s[i]]
    return summing


# b
def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1
    dicty = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e"}
    string = ""
    collector = n
    for i in range(k-1,-1,-1):
        wholes = collector//5**i
        string += dicty[wholes]
        collector -= (wholes*(5**i))
    return string


# c
def sort_strings1(lst, k):
    helping = [0 for i in range(5**k)]
    new_list = []
    for string in lst:
        helping[string_to_int(string)]+=1
    for index in range(len(helping)):
        if helping[index] != 0:
            for count in range(helping[index]):
                new_list.append(index)
    for i in range(len(new_list)):
       new_list[i] = int_to_string(k,new_list[i])
    return new_list


# e
def sort_strings2(lst, k):
    new_list = []
    for i in range(5**k):
        for g in range(len(lst)):
            if i == string_to_int(lst[g]):
                new_list.append(i)
    for item in range(len(new_list)):
        new_list[item] = int_to_string(k,new_list[item])
    return new_list


########
# Tester
########

def test():
    # q2
    if complete_graph(4) != \
           [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]:
        print("error in complete_graph")

    if cycle(5) != \
           [[0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 0]]:
        print("error in cycle")

    if sum(sum(random_graph(100, 0.8)[i]) for i in range(100)) < 200:
        print("error in random_graph")

    if inv_cycle(13) != \
       [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0], \
        [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0], \
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1], \
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]:
        print("error in inv_cycle")

    if return_graph(5) != \
       [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], \
        [1, 0, 0, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0]]:
        print("error in return_graph")

    A = random_graph(100, 0.9)
    for _ in range(10):
        v = random.randint(0, 99)
        u = random_step(A, v)
        if not A[v][u]:
            print("error in random_step")

    if 0 in walk_histogram(inv_cycle(13)) or \
       0 in walk_histogram(cycle(10)):
        print("error in walk_histogram")

    
    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    missing = find_missing([0,1,2,3,5], 5)
    if missing != 4:
        print("error in find_missing")

    pos = find([30, 40, 50, 60, 10, 20], 60)
    if pos != 3:
        print("error in find")

    pos = find([30, 40, 50, 60, 10, 20], 0)
    if pos != None:
        print("error in find")

    pos = find2([30, 40, 50, 60, 60, 20], 60)
    if pos != 3 and pos != 4:
        print("error in find2")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")
